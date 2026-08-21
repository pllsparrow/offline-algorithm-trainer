#!/usr/bin/env python3
"""ACM judge: run a solution as an independent process and compare stdout.

All problems use the text protocol. Each test case carries a stdin payload and
an expected stdout payload. The judge normalises whitespace (collapsing runs of
whitespace into single spaces) so trailing newlines do not cause false
failures, then compares the result text for exact equality.
"""
import json
from collections import Counter
import subprocess
import sys


def comparable_text(text: str) -> str:
    """Collapse runs of whitespace into single spaces and strip the ends."""
    return " ".join(text.split())


def valid_top_k_frequent(stdin: str, actual: str) -> bool:
    """Accept every valid choice when frequencies tie at the k-th boundary."""
    try:
        tokens = list(map(int, stdin.split()))
        count = tokens[0]
        values = tokens[1 : count + 1]
        k = tokens[count + 1]
        answer = list(map(int, actual.split()))
    except (IndexError, ValueError):
        return False

    frequencies = Counter(values)
    if len(answer) != k or len(set(answer)) != k or answer != sorted(answer):
        return False
    if not 1 <= k <= len(frequencies):
        return False

    cutoff = sorted(frequencies.values(), reverse=True)[k - 1]
    required = {value for value, frequency in frequencies.items() if frequency > cutoff}
    allowed = {value for value, frequency in frequencies.items() if frequency >= cutoff}
    selected = set(answer)
    return required <= selected <= allowed


def valid_k_closest(stdin: str, actual: str) -> bool:
    """Accept any valid multiset of the k closest input points."""
    try:
        input_values = list(map(int, stdin.split()))
        point_count = input_values[0]
        coordinate_end = 1 + 2 * point_count
        if len(input_values) != coordinate_end + 1:
            return False

        points = [
            (input_values[index], input_values[index + 1])
            for index in range(1, coordinate_end, 2)
        ]
        k = input_values[coordinate_end]
        output_values = list(map(int, actual.split()))
    except (IndexError, ValueError):
        return False

    if not 1 <= k <= point_count or len(output_values) != 2 * k:
        return False

    selected = [
        (output_values[index], output_values[index + 1])
        for index in range(0, len(output_values), 2)
    ]
    available_counts = Counter(points)
    selected_counts = Counter(selected)
    if any(count > available_counts[point] for point, count in selected_counts.items()):
        return False

    def squared_distance(point: tuple[int, int]) -> int:
        return point[0] * point[0] + point[1] * point[1]

    cutoff = sorted(squared_distance(point) for point in points)[k - 1]
    if any(squared_distance(point) > cutoff for point in selected):
        return False

    required_counts = Counter(
        point for point in points if squared_distance(point) < cutoff
    )
    return all(
        selected_counts[point] >= count for point, count in required_counts.items()
    )


def output_matches(validator: str | None, stdin: str, actual: str, expected: str) -> bool:
    """Use semantic validation where multiple outputs are correct."""
    if validator == "top_k_frequent":
        return valid_top_k_frequent(stdin, actual)
    if validator == "k_closest":
        return valid_k_closest(stdin, actual)
    return comparable_text(actual) == comparable_text(expected)


def main() -> None:
    payload = json.load(sys.stdin)
    code = payload["code"]
    cases = payload["cases"]
    validator = payload.get("validator")
    only_case = payload.get("case")
    run_all = payload.get("run_all", False)
    debug = payload.get("debug", False)
    results = []
    for index, case in enumerate(cases, start=1):
        if only_case is not None and index != only_case:
            continue
        expected = case["stdout"]
        passed = False
        actual = "[no output]"
        stderr = ""
        returncode = None
        try:
            process = subprocess.run(
                [sys.executable, "-c", code],
                input=case["stdin"],
                text=True,
                capture_output=True,
                timeout=3,
            )
            actual = process.stdout
            stderr = process.stderr
            returncode = process.returncode
            if process.returncode != 0:
                actual = f"[process exited {process.returncode}]\n{process.stderr}"
            else:
                passed = output_matches(validator, case["stdin"], actual, expected)
        except subprocess.TimeoutExpired:
            actual = "[time limit exceeded]"
        results.append(
            {
                "case": index,
                "passed": passed,
                "input": {"stdin": case["stdin"]},
                "expected": expected,
                "actual": actual,
                "stderr": stderr if debug else "",
                "returncode": returncode,
            }
        )
        if not passed and not run_all:
            break
    print(
        json.dumps(
            {
                "ok": bool(results) and all(item["passed"] for item in results),
                "slug": payload.get("slug"),
                "mode": "acm",
                "selected_case": only_case,
                "results": results,
                "total_cases": len(cases),
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
