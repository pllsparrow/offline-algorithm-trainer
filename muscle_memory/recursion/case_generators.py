#!/usr/bin/env python3
"""Deterministic cases for recursion and backtracking drills."""

from __future__ import annotations

import itertools
import random
from dataclasses import dataclass


@dataclass(frozen=True)
class Case:
    stdin: str
    expected: str
    size: int
    category: str


EXERCISES = {
    "r01": ("Sum of Digits", "r01_sum_of_digits.py"),
    "r02": ("Reverse String", "r02_reverse_string.py"),
    "r03": ("Recursive Array Sum", "r03_recursive_array_sum.py"),
    "r04": ("Recursive Array Maximum", "r04_recursive_array_maximum.py"),
    "r05": ("Count Target Occurrences", "r05_count_target_occurrences.py"),
    "r06": ("Remove Adjacent Duplicates", "r06_remove_adjacent_duplicates.py"),
    "r07": ("Tower of Hanoi Move Count", "r07_tower_of_hanoi_move_count.py"),
    "r08": ("Restore IP Addresses", "r08_restore_ip_addresses.py"),
    "r09": ("Merge Sort", "r09_merge_sort.py"),
    "r10": ("Count Inversions", "r10_count_inversions.py"),
    "r11": ("Recursive Tree Traversals", "r11_recursive_tree_traversals.py"),
    "r12": ("Root-to-Leaf Path Sums", "r12_root_to_leaf_path_sums.py"),
    "r13": ("Count Leaf Nodes", "r13_count_leaf_nodes.py"),
    "r14": ("Sum of Left Leaves", "r14_sum_of_left_leaves.py"),
    "r15": ("Nodes at Depth K", "r15_nodes_at_depth_k.py"),
    "r16": ("Deepest Leaves Sum", "r16_deepest_leaves_sum.py"),
    "r17": ("Root-to-Leaf Numbers", "r17_root_to_leaf_numbers.py"),
    "r18": ("Prune Zero-Only Subtrees", "r18_prune_zero_only_subtrees.py"),
    "r19": ("Evaluate Expression Tree", "r19_evaluate_expression_tree.py"),
    "r20": ("Binary Tree Tilt", "r20_binary_tree_tilt.py"),
}


def _ints(values: list[int] | tuple[int, ...]) -> str:
    return " ".join(map(str, values))


def _lines(rows: list[tuple[int, ...]] | list[str]) -> str:
    return "\n".join(_ints(row) if isinstance(row, tuple) else row for row in rows) + "\n"


def _build_r01() -> list[Case]:
    rng = random.Random(2101)
    values = [0, 7, -12345] + [rng.randint(-(10**17), 10**17) for _ in range(46)]
    return [Case(f"{value}\n", f"{sum(map(int, str(abs(value))))}\n", len(str(abs(value))), "zero, sign, and long integers") for value in values]


def _build_r02() -> list[Case]:
    rng = random.Random(2102)
    alphabet = "abcXYZ 012"
    values = ["", "a", "recursion"] + ["".join(rng.choice(alphabet) for _ in range(rng.randint(2, 180))) for _ in range(46)]
    return [Case(text + "\n", text[::-1] + "\n", len(text), "empty, spaces, and repeated characters") for text in values]


def _build_r03() -> list[Case]:
    return [Case(f"{len(values)}\n{_ints(values)}\n", f"{sum(values)}\n", len(values), "empty, signs, and repeated values") for values in _arrays(2103)]


def _build_r04() -> list[Case]:
    arrays = [[0], [-7], [2, 1]] + _arrays(2104)[3:]
    return [Case(f"{len(values)}\n{_ints(values)}\n", f"{max(values)}\n", len(values), "single, negative, and repeated values") for values in arrays]


def _build_r05() -> list[Case]:
    rng = random.Random(2105)
    cases = []
    for index in range(49):
        size = index if index < 3 else rng.randint(20, 500)
        values = [rng.randint(-10, 10) for _ in range(size)]
        target = rng.randint(-12, 12)
        cases.append(Case(f"{size} {target}\n{_ints(values)}\n", f"{values.count(target)}\n", size, "absent, repeated, and boundary targets"))
    return cases


def _build_r06() -> list[Case]:
    rng = random.Random(2106)
    values = ["", "a", "aaabccddd"] + ["".join(rng.choice("aabbccXYZ") for _ in range(rng.randint(10, 300))) for _ in range(46)]
    return [Case(text + "\n", "".join(ch for index, ch in enumerate(text) if index == 0 or ch != text[index - 1]) + "\n", len(text), "runs, boundaries, and mixed characters") for text in values]


def _combinations(candidates: list[int], target: int) -> list[tuple[int, ...]]:
    answers: list[tuple[int, ...]] = []
    def visit(start: int, remaining: int, path: tuple[int, ...]) -> None:
        if remaining == 0:
            answers.append(path)
            return
        for index in range(start, len(candidates)):
            value = candidates[index]
            if value > remaining:
                break
            visit(index, remaining - value, path + (value,))
    visit(0, target, ())
    return answers


def _build_r07() -> list[Case]:
    return [Case(f"{disks}\n", f"{2**disks - 1}\n", disks, "recurrence growth") for disks in range(1, 50)]


def _restore_ip(text: str) -> list[str]:
    answers = []
    for a in range(1, 4):
        for b in range(a + 1, a + 4):
            for c in range(b + 1, b + 4):
                parts = [text[:a], text[a:b], text[b:c], text[c:]]
                if all(part and len(part) <= 3 and (part == "0" or not part.startswith("0")) and int(part) <= 255 for part in parts):
                    answers.append(".".join(parts))
    return sorted(answers)


def _build_r08() -> list[Case]:
    rng = random.Random(2108)
    values = ["0000", "25525511135", "101023"]
    seen = set(values)
    while len(values) < 49:
        text = "".join(rng.choice("0123456789") for _ in range(rng.randint(4, 12)))
        if text not in seen:
            seen.add(text)
            values.append(text)
    return [Case(text + "\n", _lines(_restore_ip(text)), len(text), "leading zeros and segment bounds") for text in values]


def _arrays(seed: int) -> list[list[int]]:
    rng = random.Random(seed)
    arrays = [[], [1], [2, 1]]
    arrays.extend([rng.choices(range(-100, 101), k=rng.randint(20, 500)) for _ in range(46)])
    return arrays


def _build_r09() -> list[Case]:
    return [Case(f"{len(values)}\n{_ints(values)}\n", _ints(sorted(values)) + "\n", len(values), "duplicates and ordering") for values in _arrays(2109)]


def _inversions(values: list[int]) -> int:
    return sum(values[left] > values[right] for left in range(len(values)) for right in range(left + 1, len(values)))


def _build_r10() -> list[Case]:
    return [Case(f"{len(values)}\n{_ints(values)}\n", f"{_inversions(values)}\n", len(values), "sorted, reversed, and duplicate values") for values in _arrays(2110)]


def _tree_depth(nodes: list[str]) -> int:
    def visit(index: int) -> int:
        if index >= len(nodes) or nodes[index] == "null":
            return 0
        return 1 + max(visit(index * 2 + 1), visit(index * 2 + 2))
    return visit(0)


def _trees(seed: int) -> list[list[str]]:
    rng = random.Random(seed)
    trees = [[], ["1"], ["1", "2", "3", "4", "null", "null", "5"]]
    seen = {tuple(nodes) for nodes in trees}
    while len(trees) < 49:
        size = rng.randint(20, 255)
        nodes = [str(rng.randint(-50, 50))]
        for index in range(1, size):
            parent = (index - 1) // 2
            nodes.append("null" if nodes[parent] == "null" or rng.random() < 0.28 else str(rng.randint(-50, 50)))
        while nodes and nodes[-1] == "null":
            nodes.pop()
        key = tuple(nodes)
        if key in seen:
            continue
        seen.add(key)
        trees.append(nodes)
    return trees


def _build_r11() -> list[Case]:
    cases = []
    for nodes in _trees(2111):
        orders = [[], [], []]
        def visit(index: int) -> None:
            if index >= len(nodes) or nodes[index] == "null":
                return
            value = int(nodes[index])
            orders[0].append(value)
            visit(index * 2 + 1)
            orders[1].append(value)
            visit(index * 2 + 2)
            orders[2].append(value)
        visit(0)
        expected = "".join(_ints(order) + "\n" for order in orders)
        cases.append(Case(f"{len(nodes)}\n{' '.join(nodes)}\n", expected, len(nodes), "preorder, inorder, and postorder"))
    return cases


def _path_sums(nodes: list[str]) -> list[int]:
    answers = []
    def visit(index: int, total: int) -> None:
        if index >= len(nodes) or nodes[index] == "null":
            return
        total += int(nodes[index])
        left, right = index * 2 + 1, index * 2 + 2
        if (left >= len(nodes) or nodes[left] == "null") and (right >= len(nodes) or nodes[right] == "null"):
            answers.append(total)
            return
        visit(left, total)
        visit(right, total)
    visit(0, 0)
    return sorted(answers)


def _build_r12() -> list[Case]:
    return [Case(f"{len(nodes)}\n{' '.join(nodes)}\n", _ints(_path_sums(nodes)) + "\n", len(nodes), "negative values and sparse leaves") for nodes in _trees(2112)]


def _present(nodes: list[str], index: int) -> bool:
    return index < len(nodes) and nodes[index] != "null"


def _build_r13() -> list[Case]:
    cases = []
    for nodes in _trees(2113):
        leaves = sum(
            _present(nodes, index)
            and not _present(nodes, index * 2 + 1)
            and not _present(nodes, index * 2 + 2)
            for index in range(len(nodes))
        )
        cases.append(Case(f"{len(nodes)}\n{' '.join(nodes)}\n", f"{leaves}\n", len(nodes), "empty, one-sided, and branching trees"))
    return cases


def _build_r14() -> list[Case]:
    cases = []
    for nodes in _trees(2114):
        total = 0
        for parent in range(len(nodes)):
            left = parent * 2 + 1
            if _present(nodes, parent) and _present(nodes, left) and not _present(nodes, left * 2 + 1) and not _present(nodes, left * 2 + 2):
                total += int(nodes[left])
        cases.append(Case(f"{len(nodes)}\n{' '.join(nodes)}\n", f"{total}\n", len(nodes), "left-child context and negative leaves"))
    return cases


def _build_r15() -> list[Case]:
    cases = []
    for index, nodes in enumerate(_trees(2115)):
        depth = index % 10
        values = [int(value) for position, value in enumerate(nodes) if value != "null" and (position + 1).bit_length() - 1 == depth]
        cases.append(Case(f"{len(nodes)} {depth}\n{' '.join(nodes)}\n", _ints(values) + "\n", len(nodes), "missing levels and sparse trees"))
    return cases


def _build_r16() -> list[Case]:
    cases = []
    for nodes in _trees(2116):
        present = [(position, int(value)) for position, value in enumerate(nodes) if value != "null"]
        deepest = max(((position + 1).bit_length() - 1 for position, _ in present), default=-1)
        total = sum(value for position, value in present if (position + 1).bit_length() - 1 == deepest)
        cases.append(Case(f"{len(nodes)}\n{' '.join(nodes)}\n", f"{total}\n", len(nodes), "deepest-level aggregation"))
    return cases


def _digit_trees() -> list[list[str]]:
    answers = []
    seen = set()
    seed = 2117
    while len(answers) < 49:
        for nodes in _trees(seed):
            digits = [str(abs(int(value)) % 10) if value != "null" else value for value in nodes]
            key = tuple(digits)
            if key not in seen:
                seen.add(key)
                answers.append(digits)
                if len(answers) == 49:
                    break
        seed += 1
    return answers


def _build_r17() -> list[Case]:
    cases = []
    for nodes in _digit_trees():
        total = 0
        def visit(index: int, number: int) -> None:
            nonlocal total
            if not _present(nodes, index):
                return
            number = number * 10 + int(nodes[index])
            if not _present(nodes, index * 2 + 1) and not _present(nodes, index * 2 + 2):
                total += number
                return
            visit(index * 2 + 1, number)
            visit(index * 2 + 2, number)
        visit(0, 0)
        cases.append(Case(f"{len(nodes)}\n{' '.join(nodes)}\n", f"{total}\n", len(nodes), "path-state place values"))
    return cases


def _zero_trees() -> list[list[str]]:
    rng = random.Random(2118)
    trees = [[], ["0"], ["1"]]
    while len(trees) < 49:
        size = rng.randint(15, 127)
        nodes = [str(rng.randint(0, 1))]
        for index in range(1, size):
            nodes.append("null" if nodes[(index - 1) // 2] == "null" or rng.random() < 0.22 else str(rng.randint(0, 1)))
        while nodes and nodes[-1] == "null":
            nodes.pop()
        if nodes not in trees:
            trees.append(nodes)
    return trees


def _pruned(nodes: list[str]) -> list[str]:
    kept = set()
    def visit(index: int) -> bool:
        if not _present(nodes, index):
            return False
        keep = nodes[index] == "1" or visit(index * 2 + 1) or visit(index * 2 + 2)
        if keep:
            kept.add(index)
        return keep
    visit(0)
    if not kept:
        return []
    answer = [nodes[index] if index in kept else "null" for index in range(max(kept) + 1)]
    return answer


def _build_r18() -> list[Case]:
    return [Case(f"{len(nodes)}\n{' '.join(nodes)}\n", f"{len(_pruned(nodes))}\n{' '.join(_pruned(nodes))}\n", len(nodes), "postorder structural pruning") for nodes in _zero_trees()]


def _expression_cases() -> list[tuple[list[str], int]]:
    rng = random.Random(2119)
    cases = []
    for index in range(49):
        depth = 1 + index % 5
        leaf_start = 2**depth - 1
        tokens = [rng.choice(["+", "-", "*"]) for _ in range(leaf_start)]
        tokens += [str(rng.randint(-5, 9)) for _ in range(2**depth)]
        def evaluate(position: int) -> int:
            token = tokens[position]
            if token not in {"+", "-", "*"}:
                return int(token)
            left, right = evaluate(position * 2 + 1), evaluate(position * 2 + 2)
            return left + right if token == "+" else left - right if token == "-" else left * right
        cases.append((tokens, evaluate(0)))
    return cases


def _build_r19() -> list[Case]:
    return [Case(f"{len(tokens)}\n{' '.join(tokens)}\n", f"{answer}\n", len(tokens), "recursive expression evaluation") for tokens, answer in _expression_cases()]


def _build_r20() -> list[Case]:
    cases = []
    for nodes in _trees(2120):
        tilt = 0
        def visit(index: int) -> int:
            nonlocal tilt
            if not _present(nodes, index):
                return 0
            left, right = visit(index * 2 + 1), visit(index * 2 + 2)
            tilt += abs(left - right)
            return left + right + int(nodes[index])
        visit(0)
        cases.append(Case(f"{len(nodes)}\n{' '.join(nodes)}\n", f"{tilt}\n", len(nodes), "subtree sums and postorder aggregation"))
    return cases


BUILDERS = {exercise_id: globals()[f"_build_{exercise_id}"] for exercise_id in EXERCISES}


def build_cases(exercise_id: str) -> list[Case]:
    return BUILDERS[exercise_id]()
