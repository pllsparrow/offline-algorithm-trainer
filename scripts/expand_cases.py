#!/usr/bin/env python3
"""Expand the canonical test corpus with deterministic, oracle-checked cases.

The script expects a checkout of wislertt/leetcode-py. It mutates the existing
curated cases, rejects candidates outside each problem's input contract, and
uses the reference implementation to compute the expected value. The ACM text
spec is rebuilt separately by scripts/build_acm.py.
"""
from __future__ import annotations

import argparse
import copy
import importlib.util
import inspect
import json
import random
import re
import sys
import types
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, values):
        dummy = cls()
        tail = dummy
        for value in values:
            tail.next = cls(value)
            tail = tail.next
        return dummy.next

    def to_list(self):
        values = []
        seen = set()
        node = self
        while node is not None and id(node) not in seen:
            seen.add(id(node))
            values.append(node.val)
            node = node.next
        return values

    @classmethod
    def __class_getitem__(cls, item):
        return cls


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_list(cls, values):
        if not values or values[0] is None:
            return None
        root = cls(values[0])
        queue = [root]
        index = 1
        while queue and index < len(values):
            node = queue.pop(0)
            if index < len(values) and values[index] is not None:
                node.left = cls(values[index])
                queue.append(node.left)
            index += 1
            if index < len(values) and values[index] is not None:
                node.right = cls(values[index])
                queue.append(node.right)
            index += 1
        return root

    def to_list(self):
        values = []
        queue = [self]
        while queue:
            node = queue.pop(0)
            if node is None:
                values.append(None)
                continue
            values.append(node.val)
            queue.extend((node.left, node.right))
        while values and values[-1] is None:
            values.pop()
        return values

    def find_node(self, value):
        if self.val == value:
            return self
        found = self.left.find_node(value) if self.left else None
        return found or (self.right.find_node(value) if self.right else None)

    @classmethod
    def __class_getitem__(cls, item):
        return cls


class GraphNode:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = [] if neighbors is None else neighbors

    @classmethod
    def from_adjacency_list(cls, adjacency):
        if not adjacency:
            return None
        nodes = [cls(index + 1) for index in range(len(adjacency))]
        for index, neighbors in enumerate(adjacency):
            nodes[index].neighbors = [nodes[value - 1] for value in neighbors]
        return nodes[0]

    @staticmethod
    def to_adjacency_list(node):
        if node is None:
            return []
        found = {}
        queue = [node]
        while queue:
            current = queue.pop(0)
            if current.val in found:
                continue
            found[current.val] = sorted(neighbor.val for neighbor in current.neighbors)
            queue.extend(current.neighbors)
        return [found.get(index, []) for index in range(1, max(found) + 1)]


class DoublyListNode(ListNode):
    def __init__(self, val=0, prev=None, next=None):
        super().__init__(val, next)
        self.prev = prev


class DictTree:
    @classmethod
    def __class_getitem__(cls, item):
        return cls


def install_reference_stubs() -> None:
    package = types.ModuleType("leetcode_py")
    package.ListNode = ListNode
    package.TreeNode = TreeNode
    package.GraphNode = GraphNode
    structures = types.ModuleType("leetcode_py.data_structures")
    structures.DictTree = DictTree
    structures.RecursiveDict = dict
    doubly = types.ModuleType("leetcode_py.data_structures.doubly_list_node")
    doubly.DoublyListNode = DoublyListNode
    sys.modules.update(
        {
            "leetcode_py": package,
            "leetcode_py.data_structures": structures,
            "leetcode_py.data_structures.doubly_list_node": doubly,
        }
    )


def reference_directory(reference: Path, slug: str) -> Path:
    name = "three_sum" if slug == "3sum" else slug.replace("-", "_")
    return reference / "leetcode" / name


def load_solution(reference: Path, slug: str):
    path = reference_directory(reference, slug) / "solution.py"
    spec = importlib.util.spec_from_file_location(f"case_oracle_{slug.replace('-', '_')}", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


LIST_ARGUMENTS = {
    "reverse-linked-list": (0,),
    "merge-two-sorted-lists": (0, 1),
    "reorder-list": (0,),
    "remove-nth-node-from-end-of-list": (0,),
    "add-two-numbers": (0, 1),
    "merge-k-sorted-lists": (0,),
    "reverse-nodes-in-k-group": (0,),
}
MUTATING_FIRST_ARGUMENT = {
    "reorder-list",
    "walls-and-gates",
    "surrounded-regions",
    "rotate-image",
    "set-matrix-zeroes",
}


def linked_list_with_cycle(values, position):
    head = ListNode.from_list(values)
    if head is None or position < 0:
        return head
    nodes = []
    current = head
    while current:
        nodes.append(current)
        current = current.next
    nodes[-1].next = nodes[position]
    return head


def random_list(module, values):
    if not values:
        return None
    nodes = [module.Node(value) for value, _ in values]
    for index, (_, random_index) in enumerate(values):
        if index + 1 < len(nodes):
            nodes[index].next = nodes[index + 1]
        if random_index is not None:
            nodes[index].random = nodes[random_index]
    return nodes[0]


def serialize_random_list(head):
    nodes = []
    current = head
    while current:
        nodes.append(current)
        current = current.next
    indices = {id(node): index for index, node in enumerate(nodes)}
    return [[node.val, None if node.random is None else indices[id(node.random)]] for node in nodes]


def find_implementation(module, method):
    for value in vars(module).values():
        if inspect.isclass(value) and callable(getattr(value, method, None)):
            return value
    raise RuntimeError(f"no class implements {method}")


def snake_case(name: str) -> str:
    return re.sub(r"(?<!^)(?=[A-Z])", "_", name).lower()


def evaluate_ops(module, spec, case):
    operations = case["ops"]
    arguments = copy.deepcopy(case["args"])
    cls = getattr(module, spec.get("class") or operations[0])
    instance = None
    output = []
    for operation, args in zip(operations, arguments):
        if operation == operations[0]:
            instance = cls(*args)
            output.append(None)
            continue
        method = getattr(instance, operation, None) or getattr(instance, snake_case(operation))
        output.append(method(*args))
    return output


def evaluate_case(module, slug, spec, case):
    if spec["method"] == "__ops__":
        return evaluate_ops(module, spec, case)

    raw_args = copy.deepcopy(case["args"])
    args = copy.deepcopy(raw_args)
    if slug == "encode-and-decode-strings":
        implementation = find_implementation(module, "encode")()
        return implementation.decode(implementation.encode(args[0]))
    if slug == "serialize-and-deserialize-binary-tree":
        codec = find_implementation(module, "serialize")()
        tree = TreeNode.from_list(args[0])
        restored = codec.deserialize(codec.serialize(tree))
        return [] if restored is None else restored.to_list()
    if slug == "linked-list-cycle":
        args = [linked_list_with_cycle(args[0], args[1])]
    elif slug == "copy-list-with-random-pointer":
        args[0] = random_list(module, args[0])
    else:
        for index in LIST_ARGUMENTS.get(slug, ()):
            if slug == "merge-k-sorted-lists":
                args[index] = [ListNode.from_list(values) for values in args[index]]
            else:
                args[index] = ListNode.from_list(args[index])
        types_ = spec.get("param_types", [])
        root = None
        for index, type_name in enumerate(types_):
            if type_name == "TreeNode":
                args[index] = TreeNode.from_list(args[index])
                if root is None:
                    root = args[index]
            elif type_name == "TreeNodeValue":
                args[index] = root.find_node(args[index])
            elif type_name == "GraphNode":
                args[index] = GraphNode.from_adjacency_list(args[index])

    method = {
        "copy-list-with-random-pointer": "copy_random_list",
        "validate-binary-search-tree": "is_valid_bst",
        "word-search-ii": "find_words",
    }.get(slug, spec["method"])
    implementation = find_implementation(module, method)()
    result = getattr(implementation, method)(*args)
    if slug in MUTATING_FIRST_ARGUMENT:
        value = args[0]
        return value.to_list() if isinstance(value, ListNode) else value
    if slug == "copy-list-with-random-pointer":
        return serialize_random_list(result)
    if isinstance(result, ListNode):
        return result.to_list()
    if isinstance(result, TreeNode):
        if slug == "lowest-common-ancestor-of-a-binary-search-tree":
            return result.val
        return result.to_list()
    if isinstance(result, GraphNode):
        return GraphNode.to_adjacency_list(result)
    return result


SORTED_ARGUMENTS = {
    "two-sum-ii-input-array-is-sorted": (0,),
    "binary-search": (0,),
    "search-a-2d-matrix": (),
    "median-of-two-sorted-arrays": (0, 1),
    "merge-two-sorted-lists": (0, 1),
    "merge-k-sorted-lists": (0,),
}
POSITIVE_LISTS = {
    "container-with-most-water",
    "trapping-rain-water",
    "koko-eating-bananas",
    "largest-rectangle-in-histogram",
    "last-stone-weight",
    "coin-change",
    "coin-change-ii",
    "jump-game",
    "jump-game-ii",
    "gas-station",
    "hand-of-straights",
    "plus-one",
}
GRAPH_SLUGS = {
    "course-schedule",
    "course-schedule-ii",
    "graph-valid-tree",
    "number-of-connected-components-in-an-undirected-graph",
    "network-delay-time",
    "cheapest-flights-within-k-stops",
}
RECTANGULAR_MATRIX_SLUGS = {
    "search-a-2d-matrix",
    "word-search",
    "word-search-ii",
    "number-of-islands",
    "max-area-of-island",
    "walls-and-gates",
    "rotting-oranges",
    "pacific-atlantic-water-flow",
    "surrounded-regions",
    "swim-in-rising-water",
    "longest-increasing-path-in-a-matrix",
    "rotate-image",
    "spiral-matrix",
    "set-matrix-zeroes",
}
INTERVAL_SLUGS = {
    "insert-interval",
    "merge-intervals",
    "non-overlapping-intervals",
    "meeting-rooms",
    "meeting-rooms-ii",
    "minimum-interval-to-include-each-query",
}


def is_sorted(values):
    return all(left <= right for left, right in zip(values, values[1:]))


def is_rectangular(matrix) -> bool:
    return bool(matrix) and bool(matrix[0]) and all(
        isinstance(row, list) and len(row) == len(matrix[0]) for row in matrix
    )


def is_bst(values) -> bool:
    root = TreeNode.from_list(values)

    def visit(node, low, high):
        if node is None:
            return True
        return low < node.val < high and visit(node.left, low, node.val) and visit(node.right, node.val, high)

    return visit(root, float("-inf"), float("inf"))


def is_rotated_strictly_increasing(values) -> bool:
    if not values or len(set(values)) != len(values):
        return False
    drops = sum(left > right for left, right in zip(values, values[1:]))
    return drops <= 1 and (drops == 0 or values[-1] < values[0])


def has_exactly_one_single(values) -> bool:
    counts = {}
    for value in values:
        counts[value] = counts.get(value, 0) + 1
    return sorted(counts.values()).count(1) == 1 and all(count in {1, 2} for count in counts.values())


def valid_ops_candidate(slug: str, case: dict) -> bool:
    operations, arguments = case["ops"], case["args"]
    if not operations or len(operations) != len(arguments):
        return False
    if slug == "lru-cache":
        return bool(arguments[0]) and arguments[0][0] > 0
    if slug == "kth-largest-element-in-a-stream":
        return len(arguments[0]) == 2 and arguments[0][0] > 0 and arguments[0][0] <= len(arguments[0][1])
    if slug == "implement-trie-prefix-tree":
        return all(
            not args or (args[0] and args[0].islower() and args[0].isalpha())
            for operation, args in zip(operations, arguments)
            if operation != operations[0]
        )
    if slug == "design-add-and-search-words-data-structure":
        return all(
            not args or (args[0] and all(char == "." or "a" <= char <= "z" for char in args[0]))
            for operation, args in zip(operations, arguments)
            if operation != operations[0]
        )
    if slug == "detect-squares":
        return all(
            not args or (
                len(args[0]) == 2
                and all(isinstance(value, int) and 0 <= value <= 1000 for value in args[0])
            )
            for operation, args in zip(operations, arguments)
            if operation != operations[0]
        )
    return True


def valid_candidate(slug: str, args) -> bool:
    if slug == "generate-parentheses":
        return isinstance(args[0], int) and 0 <= args[0] <= 8
    if slug == "n-queens":
        return isinstance(args[0], int) and 1 <= args[0] <= 10
    if slug == "happy-number":
        return isinstance(args[0], int) and args[0] > 0
    if slug in {"number-of-1-bits", "reverse-bits"}:
        return isinstance(args[0], int) and 0 <= args[0] < 2**32
    if slug == "counting-bits":
        return isinstance(args[0], int) and 0 <= args[0] <= 10_000
    if slug in {"find-minimum-in-rotated-sorted-array", "search-in-rotated-sorted-array"}:
        return is_rotated_strictly_increasing(args[0])
    if slug == "valid-sudoku":
        board = args[0]
        return len(board) == 9 and all(
            len(row) == 9
            and all(len(value) == 1 and (value == "." or value in "123456789") for value in row)
            for row in board
        )
    if slug in RECTANGULAR_MATRIX_SLUGS and not is_rectangular(args[0]):
        return False
    if slug in {"rotate-image", "swim-in-rising-water"} and len(args[0]) != len(args[0][0]):
        return False
    if slug == "number-of-islands" and any(value not in {"0", "1"} for row in args[0] for value in row):
        return False
    if slug == "surrounded-regions" and any(value not in {"X", "O"} for row in args[0] for value in row):
        return False
    if slug in {"word-search", "word-search-ii"} and any(
        not isinstance(value, str) or len(value) != 1 or not value.isalpha()
        for row in args[0]
        for value in row
    ):
        return False
    if slug == "valid-parentheses":
        return all(char in "()[]{}" for char in args[0])
    if slug == "valid-parenthesis-string":
        return all(char in "()*" for char in args[0])
    if slug == "decode-ways":
        return bool(args[0]) and args[0].isdigit()
    if slug == "multiply-strings":
        return all(value.isdigit() and value and (value == "0" or value[0] != "0") for value in args)
    if slug == "letter-combinations-of-a-phone-number":
        return len(args[0]) <= 4 and all(char in "23456789" for char in args[0])
    if slug in {"lowest-common-ancestor-of-a-binary-search-tree", "kth-smallest-element-in-a-bst"} and not is_bst(args[0]):
        return False
    tree_types = {
        "invert-binary-tree",
        "maximum-depth-of-binary-tree",
        "diameter-of-binary-tree",
        "balanced-binary-tree",
        "binary-tree-level-order-traversal",
        "binary-tree-right-side-view",
        "count-good-nodes-in-binary-tree",
        "validate-binary-search-tree",
        "binary-tree-maximum-path-sum",
        "serialize-and-deserialize-binary-tree",
    }
    if slug in tree_types and args[0]:
        root = TreeNode.from_list(args[0])
        canonical = [] if root is None else root.to_list()
        supplied = list(args[0])
        while supplied and supplied[-1] is None:
            supplied.pop()
        if canonical != supplied:
            return False
    if slug in SORTED_ARGUMENTS:
        for index in SORTED_ARGUMENTS[slug]:
            value = args[index]
            if slug == "merge-k-sorted-lists":
                if any(not is_sorted(row) for row in value):
                    return False
            elif not is_sorted(value):
                return False
    if slug == "find-minimum-in-rotated-sorted-array" and not args[0]:
        return False
    if slug in {"koko-eating-bananas", "largest-rectangle-in-histogram"} and not args[0]:
        return False
    if slug in POSITIVE_LISTS:
        lists = [value for value in args if isinstance(value, list) and all(isinstance(x, int) for x in value)]
        if any(any(number < 0 for number in values) for values in lists):
            return False
    if slug in {"sliding-window-maximum", "top-k-frequent-elements", "kth-largest-element-in-an-array"}:
        return bool(args[0]) and 1 <= args[1] <= len(set(args[0])) if slug == "top-k-frequent-elements" else bool(args[0]) and 1 <= args[1] <= len(args[0])
    if slug in {"remove-nth-node-from-end-of-list", "reverse-nodes-in-k-group"}:
        return bool(args[0]) and 1 <= args[1] <= len(args[0])
    if slug == "linked-list-cycle":
        return args[1] == -1 or 0 <= args[1] < len(args[0])
    if slug == "find-the-duplicate-number":
        values = args[0]
        counts = {value: values.count(value) for value in set(values)}
        return len(values) >= 2 and all(1 <= x < len(values) for x in values) and sum(count > 1 for count in counts.values()) == 1
    if slug == "koko-eating-bananas":
        return bool(args[0]) and all(value > 0 for value in args[0]) and args[1] >= len(args[0])
    if slug in {"combination-sum", "combination-sum-ii", "coin-change"}:
        if args[1] < 0 or any(value <= 0 for value in args[0]):
            return False
    if slug == "combination-sum" and (args[1] > 40 or len(args[0]) > 12):
        return False
    if slug == "combination-sum" and len(set(args[0])) != len(args[0]):
        return False
    if slug == "coin-change-ii":
        return args[0] >= 0 and all(value > 0 for value in args[1])
    if slug == "network-delay-time":
        times, node_count, start = args
        return node_count > 0 and 1 <= start <= node_count and all(
            1 <= source <= node_count and 1 <= target <= node_count and weight >= 0
            for source, target, weight in times
        )
    if slug in GRAPH_SLUGS:
        n = args[0]
        if not isinstance(n, int) or n <= 0:
            return False
        edges = args[1]
        return all(len(edge) >= 2 and 0 <= edge[0] < n and 0 <= edge[1] < n for edge in edges)
    if slug == "car-fleet":
        return len(args[1]) == len(args[2]) and len(set(args[1])) == len(args[1]) and all(0 <= p < args[0] for p in args[1]) and all(speed > 0 for speed in args[2])
    if slug == "clone-graph":
        adjacency = args[0]
        if not adjacency:
            return True
        if any(any(neighbor < 1 or neighbor > len(adjacency) for neighbor in row) for row in adjacency):
            return False
        return all(index + 1 in adjacency[neighbor - 1] for index, row in enumerate(adjacency) for neighbor in row)
    if slug == "construct-binary-tree-from-preorder-and-inorder-traversal":
        return len(args[0]) == len(args[1]) and set(args[0]) == set(args[1]) and len(set(args[0])) == len(args[0])
    if slug == "lowest-common-ancestor-of-a-binary-search-tree":
        return args[1] in args[0] and args[2] in args[0]
    if slug == "kth-smallest-element-in-a-bst":
        return bool(args[0]) and 1 <= args[1] <= sum(value is not None for value in args[0])
    if slug in {"k-closest-points-to-origin", "kth-largest-element-in-an-array"}:
        return bool(args[0]) and 1 <= args[1] <= len(args[0])
    if slug == "add-two-numbers":
        return all(values and all(0 <= digit <= 9 for digit in values) for values in args)
    if slug == "plus-one":
        return bool(args[0]) and all(0 <= digit <= 9 for digit in args[0]) and args[0][0] != 0
    if slug == "regular-expression-matching":
        pattern = args[1]
        return (
            all("a" <= char <= "z" for char in args[0])
            and all(char in ".*" or "a" <= char <= "z" for char in pattern)
            and not pattern.startswith("*")
            and "**" not in pattern
        )
    if slug == "task-scheduler":
        return args[1] >= 0 and all(isinstance(task, str) and len(task) == 1 and task.isupper() for task in args[0])
    if slug == "permutations":
        return len(set(args[0])) == len(args[0])
    if slug == "swim-in-rising-water":
        values = [value for row in args[0] for value in row]
        return sorted(values) == list(range(len(values)))
    if slug == "gas-station":
        return bool(args[0]) and len(args[0]) == len(args[1]) and all(value >= 0 for value in args[0] + args[1])
    if slug == "partition-equal-subset-sum":
        return bool(args[0]) and all(value > 0 for value in args[0])
    if slug == "target-sum":
        return all(value >= 0 for value in args[0])
    if slug == "partition-labels":
        return bool(args[0]) and all("a" <= char <= "z" for char in args[0])
    if slug in INTERVAL_SLUGS:
        interval_args = [value for value in args if isinstance(value, list) and value and isinstance(value[0], list)]
        if any(any(len(interval) != 2 or interval[0] > interval[1] for interval in intervals) for intervals in interval_args):
            return False
        if slug == "insert-interval" and (len(args[1]) != 2 or args[1][0] > args[1][1]):
            return False
    if slug == "merge-triplets-to-form-target-triplet":
        return len(args[1]) == 3 and all(len(triplet) == 3 for triplet in args[0])
    if slug == "min-cost-to-connect-all-points":
        return bool(args[0]) and all(len(point) == 2 for point in args[0])
    if slug == "redundant-connection":
        return bool(args[0]) and all(len(edge) == 2 and min(edge) >= 1 for edge in args[0])
    if slug == "missing-number":
        values = args[0]
        return len(set(values)) == len(values) and all(0 <= value <= len(values) for value in values)
    if slug == "single-number":
        return has_exactly_one_single(args[0])
    return True


def walk_paths(value, path=()):
    if isinstance(value, list):
        for index, item in enumerate(value):
            yield from walk_paths(item, path + (index,))
    elif value is not None:
        yield path, value


def replace_at(value, path, replacement):
    target = value
    for index in path[:-1]:
        target = target[index]
    target[path[-1]] = replacement


def mutate_string(value: str, variant: int) -> str:
    if not value:
        return chr(ord("a") + variant % 26)
    if variant % 5 == 0:
        return value[::-1]
    if variant % 5 == 1:
        return value + chr(ord("a") + (variant // 5) % 26)
    if variant % 5 == 2:
        return value[1:] + value[:1]
    if variant % 5 == 3:
        return value[:-1]
    char = value[0]
    offset = 1 + (variant // 5) % 25
    if "a" <= char <= "z":
        char = chr((ord(char) - ord("a") + offset) % 26 + ord("a"))
    elif "A" <= char <= "Z":
        char = chr((ord(char) - ord("A") + offset) % 26 + ord("A"))
    return char + value[1:]


def mutate_args(slug: str, base_args, variant: int, rng: random.Random):
    args = copy.deepcopy(base_args)
    if slug in {"find-minimum-in-rotated-sorted-array", "search-in-rotated-sorted-array"}:
        length = 1 + variant % 12
        start = -(variant % 37)
        step = 1 + variant % 7
        values = [start + index * step for index in range(length)]
        rotation = variant % length
        values = values[rotation:] + values[:rotation]
        if slug == "find-minimum-in-rotated-sorted-array":
            return [values]
        target = values[variant % length] if variant % 3 else start - step
        return [values, target]
    if slug == "swim-in-rising-water":
        size = 1 + variant % 6
        values = list(range(size * size))
        random.Random(f"swim:{variant}").shuffle(values)
        return [[values[row * size : (row + 1) * size] for row in range(size)]]
    if slug == "clone-graph":
        size = 1 + variant % 8
        adjacency = [set() for _ in range(size)]
        for node in range(size - 1):
            adjacency[node].add(node + 2)
            adjacency[node + 1].add(node + 1)
        local = random.Random(f"clone:{variant}")
        for left in range(size):
            for right in range(left + 1, size):
                if local.randrange(4) == 0:
                    adjacency[left].add(right + 1)
                    adjacency[right].add(left + 1)
        return [[sorted(neighbors) for neighbors in adjacency]]
    if slug == "letter-combinations-of-a-phone-number":
        number = variant
        length = 1 + variant % 4
        digits = []
        for _ in range(length):
            digits.append(str(2 + number % 8))
            number //= 8
        return ["".join(digits)]
    if slug == "decode-ways":
        length = 1 + variant % 12
        number = str((variant * 7919 + 104729) % (10**length)).zfill(length)
        return [number]
    if slug in {"valid-parentheses", "valid-parenthesis-string"}:
        alphabet = "()[]{}" if slug == "valid-parentheses" else "()*"
        length = 1 + variant % 12
        number = variant * 104729 + 17
        chars = []
        for _ in range(length):
            chars.append(alphabet[number % len(alphabet)])
            number //= len(alphabet)
        return ["".join(chars)]
    if slug == "multiply-strings":
        left = str(variant * 7919 + 1)
        right = str(variant * variant * 104729 + 3)
        return [left, right]
    if slug == "network-delay-time":
        times, node_count, start = args
        if times and variant % 2:
            edge = times[variant % len(times)]
            edge[2] = max(1, edge[2] + 1 + variant % 31)
        elif node_count > 1:
            shift = 1 + variant % (node_count - 1)
            remap = lambda node: (node - 1 + shift) % node_count + 1
            times = [[remap(source), remap(target), weight] for source, target, weight in times]
            start = remap(start)
        return [times, node_count, start]
    if slug == "construct-binary-tree-from-preorder-and-inorder-traversal":
        delta = 1 + variant % 997
        return [[value + delta for value in traversal] for traversal in args]
    top_lists = [index for index, value in enumerate(args) if isinstance(value, list)]
    mode = variant % 10
    if top_lists and mode < 5:
        index = top_lists[variant % len(top_lists)]
        value = args[index]
        if mode == 0 and len(value) > 1:
            args[index] = value[::-1]
        elif mode == 1 and len(value) > 1:
            amount = 1 + variant % (len(value) - 1)
            args[index] = value[amount:] + value[:amount]
        elif mode == 2 and value:
            position = variant % len(value)
            args[index] = value[:position] + value[position + 1 :]
        elif mode == 3 and value:
            position = variant % len(value)
            args[index] = value + [copy.deepcopy(value[position])]
        elif mode == 4 and len(value) > 1:
            left = variant % len(value)
            right = (left + 1) % len(value)
            args[index][left], args[index][right] = args[index][right], args[index][left]
        return args

    leaves = list(walk_paths(args))
    if not leaves:
        return args
    path, value = leaves[rng.randrange(len(leaves))]
    if isinstance(value, bool):
        replacement = not value
    elif isinstance(value, int):
        delta = 1 + (variant // 9) % 97
        choices = [0, 1, -1, value + delta, value - delta, value * 2, -value, 10**3, -(10**3)]
        replacement = choices[variant % len(choices)]
    elif isinstance(value, float):
        replacement = [0.0, 1.0, -1.0, value / 2, value * 2][variant % 5]
    elif isinstance(value, str):
        replacement = mutate_string(value, variant)
    else:
        return args
    replace_at(args, path, replacement)
    return args


def json_key(value) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def ops_arg_text(value) -> str:
    if isinstance(value, bool):
        return "1" if value else "0"
    if isinstance(value, list):
        return f"{len(value)} " + " ".join(map(str, value)) if value else "0"
    return str(value)


def ops_input_key(case: dict) -> str:
    lines = [str(len(case["ops"]))]
    for operation, arguments in zip(case["ops"], case["args"]):
        suffix = " ".join(ops_arg_text(value) for value in arguments)
        lines.append(operation if not suffix else f"{operation} {suffix}")
    return "\n".join(lines) + "\n"


def expand_problem(reference: Path, slug: str, spec: dict, target: int) -> None:
    unique_cases = []
    initial_seen = set()
    for case in spec["cases"]:
        if spec["method"] == "__ops__":
            if not valid_ops_candidate(slug, case):
                continue
        elif not valid_candidate(slug, case["args"]):
            continue
        if slug == "reconstruct-itinerary" and len(case["expected"]) != len(case["args"][0]) + 1:
            continue
        key = ops_input_key(case) if "ops" in case else json_key(case["args"])
        if key not in initial_seen:
            initial_seen.add(key)
            unique_cases.append(case)
    spec["cases"] = cases = unique_cases
    target = {"generate-parentheses": 9, "n-queens": 10}.get(slug, target)
    if len(cases) >= target:
        return
    original = copy.deepcopy(cases)
    seen = set(initial_seen)
    module = load_solution(reference, slug)
    rng = random.Random(f"offline-algorithm-trainer:{slug}")
    attempts = 0
    while len(cases) < target and attempts < 20000:
        base = original[attempts % len(original)]
        attempts += 1
        if spec["method"] == "__ops__":
            candidate = copy.deepcopy(base)
            # Operation cases stay valid when their value arguments are perturbed.
            paths = [
                (path, value)
                for path, value in walk_paths(candidate["args"])
                if isinstance(value, (int, str)) and not isinstance(value, bool)
            ]
            if not paths:
                continue
            path, value = paths[rng.randrange(len(paths))]
            if isinstance(value, str):
                replacement = mutate_string(value, attempts)
            else:
                replacement = [0, 1, -1, value + 1, value * 2][attempts % 5]
            replace_at(candidate["args"], path, replacement)
            if not valid_ops_candidate(slug, candidate):
                continue
            key = ops_input_key(candidate)
        else:
            args = mutate_args(slug, base["args"], attempts, rng)
            if not valid_candidate(slug, args):
                continue
            candidate = {"args": args}
            key = json_key(args)
        if key in seen:
            continue
        try:
            candidate["expected"] = evaluate_case(module, slug, spec, candidate)
            json.dumps(candidate["expected"], allow_nan=False)
        except Exception:
            continue
        if slug == "reconstruct-itinerary" and len(candidate["expected"]) != len(candidate["args"][0]) + 1:
            continue
        seen.add(key)
        cases.append(candidate)
    if len(cases) < target:
        raise RuntimeError(f"{slug}: generated {len(cases)}/{target} cases after {attempts} attempts")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--reference", type=Path, required=True, help="Path to wislertt/leetcode-py checkout")
    parser.add_argument("--target", type=int, default=50)
    args = parser.parse_args()
    if not 46 <= args.target <= 55:
        raise SystemExit("--target must be between 46 and 55")
    install_reference_stubs()
    tests_path = DATA / "tests.json"
    tests = json.loads(tests_path.read_text(encoding="utf-8"))
    for index, (slug, spec) in enumerate(tests.items(), start=1):
        expand_problem(args.reference, slug, spec, args.target)
        print(f"[{index:03d}/150] {slug}: {len(spec['cases'])}")
    tests_path.write_text(json.dumps(tests, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
