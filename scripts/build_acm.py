#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def dump_json(value) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2) + "\n"


def json_starter(problem: dict, test_spec: dict) -> str:
    starter = problem["starter"].rstrip()
    if test_spec["method"] == "__ops__":
        adapter = (
            "from acm_support import run_operations\n\n\n"
            'if __name__ == "__main__":\n'
            f"    run_operations({test_spec['class']})\n"
        )
    else:
        adapter = (
            "from acm_support import run_solution\n\n\n"
            'if __name__ == "__main__":\n'
            f"    run_solution(Solution, {test_spec['method']!r}, "
            f"{test_spec.get('param_types', [])!r})\n"
        )
    return f"{starter}\n\n\n{adapter}"


def json_cases(test_spec: dict) -> list[dict]:
    cases = []
    for case in test_spec["cases"]:
        if test_spec["method"] == "__ops__":
            stdin_value = {"ops": case["ops"], "args": case["args"]}
        else:
            stdin_value = case.get("args", [])
        generated = {
            "stdin": json.dumps(stdin_value, ensure_ascii=False, separators=(",", ":")) + "\n",
            "expected": case["expected"],
        }
        if "expected_count" in case:
            generated["expected_count"] = case["expected_count"]
        cases.append(generated)
    return cases


def build_specs(problems: list[dict], tests: dict, text_specs: dict) -> dict:
    output = {}
    for problem in problems:
        slug = problem["slug"]
        if slug in text_specs:
            spec = dict(text_specs[slug])
            spec["protocol"] = "text"
            output[slug] = spec
            continue
        test_spec = tests[slug]
        output[slug] = {
            "protocol": "json",
            "format": (
                "stdin: one JSON positional-argument array; stdout: one JSON result"
                if test_spec["method"] != "__ops__"
                else "stdin: one JSON object with ops and args; stdout: one JSON result array"
            ),
            "starter": json_starter(problem, test_spec),
            "cases": json_cases(test_spec),
        }
    return output


def solution_path(problem: dict) -> Path:
    return ROOT / problem["path"] / "solution_acm.py"


def main() -> None:
    parser = argparse.ArgumentParser(description="Build ACM specs from the function-mode dataset")
    parser.add_argument("--check", action="store_true", help="Fail when generated specs differ")
    parser.add_argument(
        "--write-solutions",
        action="store_true",
        help="Create missing solution_acm.py starter files without overwriting work",
    )
    args = parser.parse_args()

    problems = load_json(DATA / "problems.json")
    tests = load_json(DATA / "tests.json")
    text_specs = load_json(DATA / "acm_text_specs.json")
    generated = dump_json(build_specs(problems, tests, text_specs))
    output_path = DATA / "acm_tests.json"

    if args.check:
        current = output_path.read_text(encoding="utf-8") if output_path.exists() else ""
        if current != generated:
            raise SystemExit("ACM specs are stale; run scripts/build_acm.py")
    else:
        output_path.write_text(generated, encoding="utf-8")

    if args.write_solutions:
        specs = json.loads(generated)
        created = 0
        for problem in problems:
            path = solution_path(problem)
            if path.exists():
                continue
            path.write_text(specs[problem["slug"]]["starter"], encoding="utf-8")
            created += 1
        print(f"ACM solution starters created: {created}")

    print(f"ACM specs ready: {len(problems)} problems")


if __name__ == "__main__":
    main()
