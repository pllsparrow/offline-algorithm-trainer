#!/usr/bin/env python3
"""Materialize a compact representative-example dataset from fixed ACM cases."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def describe_case(problem: dict, case: dict, position: int, first_stdout: str) -> tuple[str, str]:
    title = problem["title"]
    if position == 0:
        return "Typical case", f"Shows the standard input shape and a typical execution path for {title}."
    if position == 1:
        if case["stdout"].split() != first_stdout.split():
            return "Contrasting result", "Uses a different expected result to exercise another branch or return path."
        return "Structural variation", "Changes the input while preserving the result type to expose order-dependent implementations."

    tokens = case["stdin"].split()
    numeric_tokens = []
    for token in tokens:
        try:
            numeric_tokens.append(int(token))
        except ValueError:
            continue
    if any(value < 0 for value in numeric_tokens):
        return "Negative boundary", "Includes negative values to test comparison, sorting, or indexing across sign changes."
    if len(tokens) != len(set(tokens)):
        return "Duplicate values", "Includes duplicates to test counting, deduplication, and tie handling."
    if len(tokens) <= 4:
        return "Small boundary", "Uses a small input to verify initialization, termination, and the shortest execution path."
    return "Additional coverage", "Uses a different data distribution for extra coverage after the typical case passes."


def main() -> None:
    problems = json.loads((DATA / "problems.json").read_text(encoding="utf-8"))
    specs = json.loads((DATA / "acm_tests.json").read_text(encoding="utf-8"))
    examples = {}
    for problem in problems:
        cases = specs[problem["slug"]]["cases"][:3]
        rendered = []
        first_stdout = cases[0]["stdout"]
        for position, case in enumerate(cases):
            name, reason = describe_case(problem, case, position, first_stdout)
            rendered.append(
                {
                    "name": name,
                    "stdin": case["stdin"],
                    "stdout": case["stdout"],
                    "reason": reason,
                }
            )
        examples[problem["slug"]] = rendered
    (DATA / "examples.json").write_text(
        json.dumps(examples, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote curated starter examples for {len(examples)} problems")


if __name__ == "__main__":
    main()
