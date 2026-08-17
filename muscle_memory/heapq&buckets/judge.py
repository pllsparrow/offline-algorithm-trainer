#!/usr/bin/env python3
"""Local ACM judge for heap and bucket mental-model drills."""

from __future__ import annotations

import argparse
import subprocess
import sys
from collections import Counter
from pathlib import Path

from case_generators import EXERCISES, Case, build_cases


ROOT = Path(__file__).resolve().parent


def normalized(text: str) -> str:
    return " ".join(text.split())


def _parse_ints(text: str) -> list[int] | None:
    try:
        return list(map(int, text.split()))
    except ValueError:
        return None


def _valid_k_pairs(stdin: str, actual: str) -> bool:
    tokens = _parse_ints(stdin)
    answer = _parse_ints(actual)
    if tokens is None or answer is None:
        return False
    left_size, right_size, requested = tokens[:3]
    left = tokens[3 : 3 + left_size]
    right = tokens[3 + left_size : 3 + left_size + right_size]
    k = min(requested, left_size * right_size)
    if len(answer) != k * 2:
        return False
    selected = [(answer[index], answer[index + 1]) for index in range(0, len(answer), 2)]
    available = Counter((a, b) for a in left for b in right)
    selected_counts = Counter(selected)
    if any(amount > available[pair] for pair, amount in selected_counts.items()):
        return False
    cutoff = sorted(a + b for a in left for b in right)[k - 1]
    required = Counter((a, b) for a in left for b in right if a + b < cutoff)
    if any(selected_counts[pair] < amount for pair, amount in required.items()):
        return False
    return all(a + b <= cutoff for a, b in selected)


def _valid_reorganization(stdin: str, actual: str) -> bool:
    source = stdin.strip()
    result = actual.strip()
    possible = max(Counter(source).values()) <= (len(source) + 1) // 2
    if result == "IMPOSSIBLE":
        return not possible
    return possible and Counter(result) == Counter(source) and all(
        result[index] != result[index - 1] for index in range(1, len(result))
    )


def _valid_frequency_string(stdin: str, actual: str) -> bool:
    source = stdin.rstrip("\n")
    result = actual.strip()
    if Counter(source) != Counter(result):
        return False
    block_sizes = []
    seen = set()
    index = 0
    while index < len(result):
        character = result[index]
        if character in seen:
            return False
        seen.add(character)
        end = index + 1
        while end < len(result) and result[end] == character:
            end += 1
        block_sizes.append(end - index)
        index = end
    return block_sizes == sorted(block_sizes, reverse=True)


def output_matches(exercise_id: str, case: Case, actual: str) -> bool:
    if exercise_id == "h02":
        return _valid_k_pairs(case.stdin, actual)
    if exercise_id == "h09":
        return _valid_reorganization(case.stdin, actual)
    if exercise_id == "b01":
        return _valid_frequency_string(case.stdin, actual)
    return normalized(actual) == normalized(case.expected)


def run_case(path: Path, case: Case) -> tuple[bool, str]:
    try:
        process = subprocess.run(
            [sys.executable, str(path)],
            input=case.stdin,
            text=True,
            capture_output=True,
            timeout=5,
        )
    except subprocess.TimeoutExpired:
        return False, "[time limit exceeded]"
    if process.returncode != 0:
        return False, f"[process exited {process.returncode}]\n{process.stderr}"
    return True, process.stdout


def short(text: str, limit: int = 500) -> str:
    representation = repr(text)
    return representation if len(representation) <= limit else representation[: limit - 3] + "..."


def list_exercises() -> None:
    for exercise_id, (title, filename) in EXERCISES.items():
        print(f"{exercise_id}  {title:<36} {filename}")


def judge(exercise_id: str, selected_case: int | None, run_all: bool) -> int:
    if exercise_id not in EXERCISES:
        print(f"Unknown exercise: {exercise_id}", file=sys.stderr)
        return 2
    title, filename = EXERCISES[exercise_id]
    path = ROOT / filename
    cases = build_cases(exercise_id)
    if selected_case is not None and not 1 <= selected_case <= len(cases):
        print(f"--case must be between 1 and {len(cases)}", file=sys.stderr)
        return 2

    indexes = [selected_case - 1] if selected_case is not None else list(range(len(cases)))
    passed = 0
    failures = 0
    for index in indexes:
        case = cases[index]
        completed, actual = run_case(path, case)
        accepted = completed and output_matches(exercise_id, case, actual)
        if accepted:
            passed += 1
            continue
        failures += 1
        print(f"Not accepted: {exercise_id} {title}")
        print(f"Case {index + 1}: {case.category}, size={case.size}")
        print(f"  stdin:    {short(case.stdin)}")
        print(f"  expected: {short(case.expected)}")
        print(f"  actual:   {short(actual)}")
        relative_judge = Path(__file__).relative_to(ROOT.parents[1])
        print(f"Repeat: python3 {str(relative_judge)!r} {exercise_id} --case {index + 1}")
        if not run_all:
            print(f"Passed before failure: {passed}/99")
            return 1

    if failures == 0:
        label = f"case {selected_case}" if selected_case is not None else "all 99 cases"
        print(f"AC: {exercise_id} passed {label}")
        return 0
    print(f"Passed: {passed}/99")
    return 1


def main() -> int:
    parser = argparse.ArgumentParser(description="Judge heap and bucket mental-model drills")
    parser.add_argument("exercise", nargs="?", help="Exercise id, for example h01 or b01")
    parser.add_argument("--case", type=int, help="Run one 1-based case")
    parser.add_argument("--all", action="store_true", help="Continue after failures")
    parser.add_argument("--list", action="store_true", help="List exercises")
    args = parser.parse_args()
    if args.list or args.exercise is None:
        list_exercises()
        return 0
    return judge(args.exercise, args.case, args.all)


if __name__ == "__main__":
    raise SystemExit(main())
