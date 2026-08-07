#!/usr/bin/env python3
import json
import subprocess
import sys

from python_judge import comparable, valid_n_queens


def comparable_text(text: str) -> str:
    """Compare whitespace-separated ACM tokens, ignoring trailing whitespace."""
    return " ".join(text.split())


def main() -> None:
    payload = json.load(sys.stdin)
    code = payload["code"]
    cases = payload["cases"]
    protocol = payload.get("protocol", "text")
    slug = payload.get("slug")
    only_case = payload.get("case")
    results = []
    for index, case in enumerate(cases, start=1):
        if only_case is not None and index != only_case:
            continue
        passed = False
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
            expected = case["expected"] if protocol == "json" else case.get("stdout")
            if process.returncode == 0 and protocol == "json":
                try:
                    actual = json.loads(actual)
                    if "expected_count" in case:
                        input_args = json.loads(case["stdin"])
                        passed = valid_n_queens(actual, input_args[0], case["expected_count"])
                        expected = {"valid_solution_count": case["expected_count"]}
                    else:
                        passed = comparable(slug, actual) == comparable(slug, expected)
                except (json.JSONDecodeError, TypeError, ValueError, KeyError):
                    passed = False
            elif process.returncode == 0:
                passed = comparable_text(actual) == comparable_text(expected)
            results.append(
                {
                    "case": index,
                    "passed": passed,
                    "input": {"stdin": case["stdin"]},
                    "expected": expected,
                    "actual": actual,
                }
            )
        except subprocess.TimeoutExpired:
            results.append(
                {
                    "case": index,
                    "passed": False,
                    "input": {"stdin": case["stdin"]},
                    "expected": case["stdout"],
                    "actual": "[time limit exceeded]",
                }
            )
        if not passed and not payload.get("run_all"):
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
