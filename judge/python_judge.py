#!/usr/bin/env python3
import contextlib
import copy
import io
import json
import signal
import sys
import traceback
from collections import deque
from pathlib import Path
from typing import List, Optional

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Node:
    def __init__(self, val=0, next=None, random=None, neighbors=None):
        self.val = val
        if isinstance(next, list) and neighbors is None:
            neighbors = next
            next = None
        self.next = next
        self.random = random
        self.neighbors = neighbors if neighbors is not None else []


def normalize(value):
    if isinstance(value, ListNode):
        out = []
        seen = set()
        while value and id(value) not in seen:
            seen.add(id(value))
            out.append(value.val)
            value = value.next
        return out
    if isinstance(value, TreeNode):
        out = []
        q = deque([value])
        while q:
            node = q.popleft()
            if node is None:
                out.append(None)
                continue
            out.append(node.val)
            q.append(node.left)
            q.append(node.right)
        while out and out[-1] is None:
            out.pop()
        return out
    if isinstance(value, Node):
        if value.neighbors:
            return graph_to_adj(value)
        return random_list_to_list(value)
    if isinstance(value, tuple):
        return [normalize(v) for v in value]
    if isinstance(value, list):
        return [normalize(v) for v in value]
    if isinstance(value, dict):
        return {k: normalize(v) for k, v in value.items()}
    return value


def comparable(slug, value):
    empty_as_list = {
        "reverse-linked-list",
        "merge-two-sorted-lists",
        "remove-nth-node-from-end-of-list",
        "add-two-numbers",
        "merge-k-sorted-lists",
        "reverse-nodes-in-k-group",
        "invert-binary-tree",
        "construct-binary-tree-from-preorder-and-inorder-traversal",
        "serialize-and-deserialize-binary-tree",
        "clone-graph",
        "copy-list-with-random-pointer",
    }
    if value is None and slug in empty_as_list:
        return []
    value = normalize(value)
    nested_orderless = {
        "group-anagrams",
        "3sum",
        "subsets",
        "subsets-ii",
        "permutations",
        "combination-sum",
        "combination-sum-ii",
        "palindrome-partitioning",
        "k-closest-points-to-origin",
        "pacific-atlantic-water-flow",
    }
    item_orderless = {"n-queens", "word-search-ii"}
    flat_orderless = {
        "top-k-frequent-elements",
        "find-all-anagrams-in-a-string",
        "partition-labels",
        "letter-combinations-of-a-phone-number",
        "word-search-ii",
    }
    if slug in nested_orderless:
        return sorted(sorted(group) for group in value)
    if slug in item_orderless:
        return sorted(json.dumps(item, sort_keys=True) for item in value)
    if slug in flat_orderless:
        return sorted(value)
    return value


def list_to_linked(values):
    dummy = ListNode()
    cur = dummy
    for value in values or []:
        cur.next = ListNode(value)
        cur = cur.next
    return dummy.next


def list_to_tree(values):
    if not values:
        return None
    nodes = [None if value is None else TreeNode(value) for value in values]
    kids = deque(nodes[1:])
    for node in nodes:
        if node is not None:
            if kids:
                node.left = kids.popleft()
            if kids:
                node.right = kids.popleft()
    return nodes[0]


def list_to_linked_list(values):
    return [list_to_linked(item) for item in values]


def find_tree_node(root, val):
    q = deque([root])
    while q:
        node = q.popleft()
        if node is None:
            continue
        if node.val == val:
            return node
        q.append(node.left)
        q.append(node.right)
    return None


def adj_to_graph(adj):
    if not adj:
        return None
    nodes = {i + 1: Node(i + 1) for i in range(len(adj))}
    for i, neighbors in enumerate(adj, start=1):
        nodes[i].neighbors = [nodes[n] for n in neighbors]
    return nodes[1]


def graph_to_adj(node):
    if node is None:
        return []
    seen = {}
    q = deque([node])
    while q:
        cur = q.popleft()
        if cur.val in seen:
            continue
        seen[cur.val] = cur
        for neighbor in cur.neighbors:
            if neighbor.val not in seen:
                q.append(neighbor)
    return [[n.val for n in seen[i].neighbors] for i in sorted(seen)]


def valid_n_queens(solutions, n, expected_count):
    if len(solutions) != expected_count:
        return False
    seen = set()
    for board in solutions:
        if len(board) != n:
            return False
        cols = set()
        diag1 = set()
        diag2 = set()
        queens = 0
        for r, row in enumerate(board):
            if len(row) != n:
                return False
            for c, ch in enumerate(row):
                if ch == "Q":
                    queens += 1
                    if c in cols or r - c in diag1 or r + c in diag2:
                        return False
                    cols.add(c)
                    diag1.add(r - c)
                    diag2.add(r + c)
                elif ch != ".":
                    return False
        if queens != n:
            return False
        key = tuple(board)
        if key in seen:
            return False
        seen.add(key)
    return True


def list_to_random_list(nodes):
    if not nodes:
        return None
    created = [Node(item[0]) for item in nodes]
    for i, item in enumerate(nodes):
        if i + 1 < len(created):
            created[i].next = created[i + 1]
        random_index = item[1]
        if random_index is not None:
            created[i].random = created[random_index]
    return created[0]


def random_list_to_list(head):
    if head is None:
        return []
    nodes = []
    index = {}
    cur = head
    while cur:
        index[id(cur)] = len(nodes)
        nodes.append(cur)
        cur = cur.next
    out = []
    for node in nodes:
        random_index = None if node.random is None else index.get(id(node.random))
        out.append([node.val, random_index])
    return out


def convert_args(args, param_types):
    converted = []
    first_tree = None
    for pos, value in enumerate(args):
        type_name = param_types[pos] if pos < len(param_types) else ""
        if type_name == "ListNode":
            converted.append(list_to_linked(value))
        elif type_name == "List[ListNode]":
            converted.append(list_to_linked_list(value))
        elif type_name == "TreeNode":
            tree = list_to_tree(value)
            if first_tree is None:
                first_tree = tree
            converted.append(tree)
        elif type_name == "TreeNodeValue":
            converted.append(find_tree_node(first_tree, value))
        elif type_name == "GraphNode":
            converted.append(adj_to_graph(value))
        elif type_name == "RandomNode":
            converted.append(list_to_random_list(value))
        else:
            converted.append(value)
    return converted


def convert_arg(value, type_name):
    if type_name == "ListNode":
        return list_to_linked(value)
    if type_name == "TreeNode":
        return list_to_tree(value)
    if type_name == "GraphNode":
        return adj_to_graph(value)
    if type_name == "RandomNode":
        return list_to_random_list(value)
    return value


def timeout_handler(signum, frame):
    raise TimeoutError("Time limit exceeded")


def captured_call(fn, debug_stdout):
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        value = fn()
    output = buffer.getvalue()
    if debug_stdout and output:
        return value, output
    return value, ""


def main():
    slug = sys.argv[1]
    payload = json.load(sys.stdin)
    code = payload["code"]
    spec = payload["tests"]
    debug_stdout = bool(payload.get("debug_stdout"))
    run_all = bool(payload.get("run_all"))
    only_case = payload.get("case")
    namespace = {
        "List": List,
        "Optional": Optional,
        "ListNode": ListNode,
        "TreeNode": TreeNode,
        "Node": Node,
    }
    signal.signal(signal.SIGALRM, timeout_handler)
    try:
        signal.alarm(3)
        _, setup_stdout = captured_call(lambda: exec(code, namespace), debug_stdout)
        solution_cls = namespace.get("Solution")
        if solution_cls is None:
            if spec["method"] != "__ops__":
                raise ValueError("请定义 class Solution")
        method = spec["method"]
        cases = spec["cases"]
        results = []
        for idx, case in enumerate(cases, start=1):
            if only_case is not None and idx != only_case:
                continue
            original_case = copy.deepcopy(case)
            if method == "__ops__":
                class_name = spec["class"]
                target_cls = namespace.get(class_name)
                if target_cls is None:
                    raise ValueError(f"请定义 class {class_name}")
                obj = None
                actual = []
                stdout_parts = []
                for op, args in zip(case["ops"], case["args"]):
                    if op == class_name:
                        obj, call_stdout = captured_call(lambda args=args: target_cls(*args), debug_stdout)
                        actual.append(None)
                    else:
                        value, call_stdout = captured_call(lambda op=op, args=args: getattr(obj, op)(*args), debug_stdout)
                        actual.append(value)
                    if call_stdout:
                        stdout_parts.append(call_stdout)
                expected = case["expected"]
                passed = comparable(slug, actual) == comparable(slug, expected)
                results.append(
                    {
                        "case": idx,
                        "passed": passed,
                        "input": {
                            "ops": original_case["ops"],
                            "args": original_case["args"],
                        },
                        "actual": normalize(actual),
                        "expected": normalize(expected),
                        "stdout": "".join(stdout_parts),
                    }
                )
                if not passed and not run_all:
                    break
                continue
            instance = solution_cls()
            fn = getattr(instance, method, None)
            if fn is None:
                raise ValueError(f"Solution 缺少方法: {method}")
            param_types = spec.get("param_types", [])
            args = convert_args(case.get("args", []), param_types)
            expected = case["expected"]
            actual, call_stdout = captured_call(lambda: fn(*args), debug_stdout)
            if slug == "n-queens" and "expected_count" in case:
                passed = valid_n_queens(actual, args[0], case["expected_count"])
                expected = {"valid_solution_count": case["expected_count"]}
            else:
                passed = comparable(slug, actual) == comparable(slug, expected)
            results.append(
                {
                    "case": idx,
                    "passed": passed,
                    "input": {
                        "args": original_case.get("args", []),
                    },
                    "actual": normalize(actual),
                    "expected": normalize(expected),
                    "stdout": setup_stdout + call_stdout,
                }
            )
            if not passed and not run_all:
                break
        signal.alarm(0)
        print(
            json.dumps(
                {
                    "ok": bool(results) and all(r["passed"] for r in results),
                    "slug": slug,
                    "selected_case": only_case,
                    "results": results,
                    "total_cases": len(cases),
                },
                ensure_ascii=False,
            )
        )
    except Exception as exc:
        signal.alarm(0)
        print(
            json.dumps(
                {
                    "ok": False,
                    "slug": slug,
                    "error": str(exc),
                    "trace": traceback.format_exc(limit=3),
                },
                ensure_ascii=False,
            )
        )


if __name__ == "__main__":
    main()
