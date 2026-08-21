#!/usr/bin/env python3
"""Local ACM judge for recursion drills."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

from case_generators import EXERCISES, Case, build_cases


ROOT = Path(__file__).resolve().parent


def normalized(text: str) -> str:
    return "\n".join(line.rstrip() for line in text.strip().splitlines())


def run_case(path: Path, case: Case) -> tuple[bool, str]:
    try:
        process = subprocess.run([sys.executable, str(path)], input=case.stdin, text=True, capture_output=True, timeout=5)
    except subprocess.TimeoutExpired:
        return False, "[time limit exceeded]"
    if process.returncode != 0:
        return False, f"[process exited {process.returncode}]\n{process.stderr}"
    return True, process.stdout


def judge(exercise_id: str, selected_case: int | None, run_all: bool) -> int:
    if exercise_id not in EXERCISES:
        print(f"Unknown exercise: {exercise_id}", file=sys.stderr)
        return 2
    title, filename = EXERCISES[exercise_id]
    cases = build_cases(exercise_id)
    if selected_case is not None and not 1 <= selected_case <= len(cases):
        print(f"--case must be between 1 and {len(cases)}", file=sys.stderr)
        return 2
    indexes = [selected_case - 1] if selected_case else range(len(cases))
    passed = 0
    for index in indexes:
        case = cases[index]
        completed, actual = run_case(ROOT / filename, case)
        if completed and normalized(actual) == normalized(case.expected):
            passed += 1
            continue
        print(f"Not accepted: {exercise_id} {title}")
        print(f"Case {index + 1}: {case.category}, size={case.size}")
        print(f"  stdin:    {case.stdin[:500]!r}")
        print(f"  expected: {case.expected[:500]!r}")
        print(f"  actual:   {actual[:500]!r}")
        print(f"Repeat: python3 muscle_memory/recursion/judge.py {exercise_id} --case {index + 1}")
        if not run_all:
            print(f"Passed before failure: {passed}/49")
            return 1
    if passed == len(list(indexes)):
        label = f"case {selected_case}" if selected_case else "all 49 cases"
        print(f"AC: {exercise_id} passed {label}")
        return 0
    print(f"Passed: {passed}/49")
    return 1


def main() -> int:
    parser = argparse.ArgumentParser(description="Judge recursion mental-model drills")
    parser.add_argument("exercise", nargs="?")
    parser.add_argument("--case", type=int)
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--list", action="store_true")
    args = parser.parse_args()
    if args.list or args.exercise is None:
        for exercise_id, (title, filename) in EXERCISES.items():
            print(f"{exercise_id}  {title:<34} {filename}")
        return 0
    return judge(args.exercise, args.case, args.all)


if __name__ == "__main__":
    raise SystemExit(main())
