#!/usr/bin/env python3
"""ACM judge: run a solution as an independent process and compare stdout.

All problems use the text protocol. Each test case carries a stdin payload and
an expected stdout payload. The judge normalises whitespace (collapsing runs of
whitespace into single spaces) so trailing newlines do not cause false
failures, then compares the result text for exact equality.
"""
import json
import subprocess
import sys


def comparable_text(text: str) -> str:
    """Collapse runs of whitespace into single spaces and strip the ends."""
    return " ".join(text.split())


def main() -> None:
    payload = json.load(sys.stdin)
    code = payload["code"]
    cases = payload["cases"]
    only_case = payload.get("case")
    run_all = payload.get("run_all", False)
    results = []
    for index, case in enumerate(cases, start=1):
        if only_case is not None and index != only_case:
            continue
        expected = case["stdout"]
        passed = False
        actual = "[no output]"
        try:
            process = subprocess.run(
                [sys.executable, "-c", code],
                input=case["stdin"],
                text=True,
                capture_output=True,
                timeout=3,
            )
            actual = process.stdout
            if process.returncode != 0:
                actual = f"[process exited {process.returncode}]\n{process.stderr}"
            else:
                passed = comparable_text(actual) == comparable_text(expected)
        except subprocess.TimeoutExpired:
            actual = "[time limit exceeded]"
        results.append(
            {
                "case": index,
                "passed": passed,
                "input": {"stdin": case["stdin"]},
                "expected": expected,
                "actual": actual,
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
