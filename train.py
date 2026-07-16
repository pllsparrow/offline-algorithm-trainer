#!/usr/bin/env python3
import argparse
import json
import sqlite3
import subprocess
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
PROBLEMS_DIR = ROOT / "problems"
DB = DATA / "progress.sqlite3"


def load_json(path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def problems_by_slug():
    return {p["slug"]: p for p in load_json(DATA / "problems.json")}


def tests_by_slug():
    return load_json(DATA / "tests.json")


def init_db():
    DATA.mkdir(exist_ok=True)
    with sqlite3.connect(DB) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS progress (
                slug TEXT PRIMARY KEY,
                status TEXT NOT NULL DEFAULT 'todo',
                attempts INTEGER NOT NULL DEFAULT 0,
                accepted INTEGER NOT NULL DEFAULT 0,
                note TEXT NOT NULL DEFAULT '',
                updated_at TEXT NOT NULL
            )
            """
        )
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS submissions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                slug TEXT NOT NULL,
                status TEXT NOT NULL,
                code TEXT NOT NULL,
                result_json TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
            """
        )


def progress_by_slug():
    init_db()
    with sqlite3.connect(DB) as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute("SELECT * FROM progress").fetchall()
    return {row["slug"]: dict(row) for row in rows}


def update_progress(slug, code, result):
    init_db()
    now = datetime.now().isoformat(timespec="seconds")
    status = "accepted" if result.get("ok") else "attempted"
    with sqlite3.connect(DB) as conn:
        conn.execute(
            """
            INSERT INTO progress(slug, status, attempts, accepted, updated_at)
            VALUES (?, ?, 1, ?, ?)
            ON CONFLICT(slug) DO UPDATE SET
                status=excluded.status,
                attempts=progress.attempts + 1,
                accepted=progress.accepted + excluded.accepted,
                updated_at=excluded.updated_at
            """,
            (slug, status, 1 if result.get("ok") else 0, now),
        )
        conn.execute(
            """
            INSERT INTO submissions(slug, status, code, result_json, created_at)
            VALUES (?, ?, ?, ?, ?)
            """,
            (slug, status, code, json.dumps(result, ensure_ascii=False), now),
        )


def solution_path(slug):
    problem = problems_by_slug().get(slug)
    if problem and problem.get("path"):
        return ROOT / problem["path"] / "solution.py"
    return PROBLEMS_DIR / slug / "solution.py"


def render_readme(problem, test_spec):
    examples = []
    for idx, case in enumerate(test_spec.get("cases", [])[:3], start=1):
        if "args" in case:
            examples.append(
                f"### Case {idx}\n\n"
                f"```python\nargs = {case['args']!r}\nexpected = {case['expected']!r}\n```"
            )
        else:
            examples.append(
                f"### Case {idx}\n\n"
                f"```python\nops = {case['ops']!r}\nargs = {case['args']!r}\nexpected = {case['expected']!r}\n```"
            )
    hints = "\n".join(f"- {hint}" for hint in problem.get("hints", []))
    return f"""# {problem['title']}

- Category: {problem['category']}
- Difficulty: {problem['difficulty']}

## Summary

{problem['summary']}

## Python

```python
{problem['signature']}
```

## Examples

{chr(10).join(examples)}

## Hints

{hints}

## Run

```bash
python3 train.py run {problem['slug']}
```
"""


def scaffold(args):
    problems = problems_by_slug()
    tests = tests_by_slug()
    PROBLEMS_DIR.mkdir(exist_ok=True)
    created = 0
    for slug, problem in problems.items():
        problem_dir = ROOT / problem.get("path", str(PROBLEMS_DIR / slug))
        problem_dir.mkdir(exist_ok=True)
        readme_path = problem_dir / "README.md"
        if args.force or not readme_path.exists():
            readme_path.write_text(render_readme(problem, tests.get(slug, {"cases": []})), encoding="utf-8")
        path = problem_dir / "solution.py"
        if not path.exists():
            path.write_text(problem["starter"], encoding="utf-8")
            created += 1
    print(f"Scaffold ready: {len(problems)} problems, {created} new solution files.")
    print(f"Open this folder in PyCharm: {ROOT}")


def check_project(args):
    problems = problems_by_slug()
    tests = tests_by_slug()
    issues = []
    for slug, problem in problems.items():
        if slug not in tests:
            issues.append(f"{slug}: missing tests in data/tests.json")
        problem_dir = ROOT / problem.get("path", str(PROBLEMS_DIR / slug))
        if not problem_dir.exists():
            issues.append(f"{slug}: missing problem directory {problem_dir}")
            continue
        for filename in ("README.md", "solution.py"):
            if not (problem_dir / filename).exists():
                issues.append(f"{slug}: missing {problem_dir / filename}")
    extra_flat_dirs = []
    for child in PROBLEMS_DIR.iterdir():
        if child.is_dir() and child.name in problems:
            extra_flat_dirs.append(child)
    for path in extra_flat_dirs:
        issues.append(f"{path.name}: unexpected flat scaffold directory {path}")
    if issues:
        print(f"Project check failed: {len(issues)} issue(s)")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print(f"Project check passed: {len(problems)} problems, {len(tests)} test specs")
    return 0


def list_problems(args):
    problems = list(problems_by_slug().values())
    progress = progress_by_slug()
    if args.category:
        needle = args.category.lower()
        problems = [p for p in problems if needle in p["category"].lower()]
    if args.difficulty:
        problems = [p for p in problems if p["difficulty"].lower() == args.difficulty.lower()]
    for problem in problems:
        state = progress.get(problem["slug"], {})
        marker = "AC" if state.get("status") == "accepted" else "  "
        attempts = state.get("attempts", 0)
        print(f"{marker}  {problem['slug']:<48} {problem['difficulty']:<6} {attempts:>2}  {problem['category']}")


def run_judge(slug, code, *, case=None, run_all=False, debug_stdout=False):
    tests = tests_by_slug()
    if slug not in tests:
        return {"ok": False, "error": "No local tests for this problem yet."}
    proc = subprocess.run(
        [sys.executable, str(ROOT / "judge" / "python_judge.py"), slug],
        input=json.dumps(
            {
                "code": code,
                "tests": tests[slug],
                "case": case,
                "run_all": run_all,
                "debug_stdout": debug_stdout,
            },
            ensure_ascii=False,
        ),
        text=True,
        capture_output=True,
        timeout=8,
    )
    if proc.returncode != 0:
        return {"ok": False, "error": proc.stderr.strip() or proc.stdout.strip() or "Judge failed"}
    try:
        return json.loads(proc.stdout)
    except json.JSONDecodeError:
        return {"ok": False, "error": "Judge returned invalid JSON", "trace": proc.stdout}


def short_repr(value, limit=220):
    text = repr(value)
    if len(text) <= limit:
        return text
    return text[: limit - 3] + "..."


def print_case_detail(item):
    print(f"Case {item['case']}: fail")
    case_input = item.get("input", {})
    if "ops" in case_input:
        print(f"  ops:      {short_repr(case_input['ops'])}")
        print(f"  args:     {short_repr(case_input['args'])}")
    else:
        print(f"  args:     {short_repr(case_input.get('args', []))}")
    print(f"  expected: {short_repr(item['expected'])}")
    print(f"  actual:   {short_repr(item['actual'])}")
    if item.get("stdout"):
        print("  stdout:")
        for line in item["stdout"].rstrip().splitlines():
            print(f"    {line}")


def print_result(result, *, show_passed=False, show_all_failures=False):
    if result.get("ok"):
        total = result.get("total_cases", len(result.get("results", [])))
        selected = result.get("selected_case")
        if selected is None:
            print(f"AC: all {total} local tests passed")
        else:
            print(f"AC: case {selected} passed")
    else:
        print("Not accepted")
    if result.get("error"):
        print()
        print(result["error"])
        if result.get("trace"):
            print(result["trace"])
        return
    results = result.get("results", [])
    passed_count = sum(1 for item in results if item["passed"])
    total = result.get("total_cases", len(results))
    if results:
        if result.get("selected_case") is None:
            print(f"Passed: {passed_count}/{total}")
        else:
            print(f"Passed: {passed_count}/{len(results)} selected")
    for item in results:
        if item["passed"]:
            if show_passed:
                print(f"Case {item['case']}: pass")
                if item.get("stdout"):
                    print("  stdout:")
                    for line in item["stdout"].rstrip().splitlines():
                        print(f"    {line}")
            continue
        print_case_detail(item)
        if result.get("selected_case") is None:
            print()
            print(f"Debug this case only: python3 train.py run {result['slug']} --case {item['case']} --debug")
        if not show_all_failures:
            break


def run_problem(args):
    problems = problems_by_slug()
    if args.slug not in problems:
        print(f"Unknown problem: {args.slug}", file=sys.stderr)
        return 2
    tests = tests_by_slug().get(args.slug)
    if args.case is not None:
        if args.case < 1:
            print("--case must be a 1-based test case number", file=sys.stderr)
            return 2
        if tests and args.case > len(tests.get("cases", [])):
            print(f"{args.slug} only has {len(tests.get('cases', []))} local test cases", file=sys.stderr)
            return 2
    path = Path(args.file) if args.file else solution_path(args.slug)
    if not path.exists():
        print(f"Missing solution file: {path}", file=sys.stderr)
        print(f"Run: python3 train.py scaffold", file=sys.stderr)
        return 2
    code = path.read_text(encoding="utf-8")
    result = run_judge(args.slug, code, case=args.case, run_all=args.all, debug_stdout=args.debug)
    update_progress(args.slug, code, result)
    print_result(result, show_passed=args.all or args.debug, show_all_failures=args.all)
    return 0 if result.get("ok") else 1


def show_status(args):
    problems = problems_by_slug()
    progress = progress_by_slug()
    accepted = sum(1 for p in progress.values() if p.get("status") == "accepted")
    attempted = sum(1 for p in progress.values() if p.get("attempts", 0) > 0)
    print(f"Accepted: {accepted}/{len(problems)}")
    print(f"Attempted: {attempted}/{len(problems)}")


def show_problem(args):
    problems = problems_by_slug()
    problem = problems.get(args.slug)
    if not problem:
        print(f"Unknown problem: {args.slug}", file=sys.stderr)
        return 2
    print(f"{problem['title']} [{problem['difficulty']}]")
    print(problem["category"])
    print()
    print(problem["summary"])
    print()
    print(problem["signature"])
    print()
    for hint in problem.get("hints", []):
        print(f"- {hint}")
    print()
    print(f"File: {solution_path(args.slug)}")
    return 0


def main():
    parser = argparse.ArgumentParser(description="Offline algorithm training CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("scaffold", help="Create PyCharm-friendly problem folders")
    p.add_argument("--force", action="store_true", help="Rewrite README files")
    p.set_defaults(func=scaffold)

    p = sub.add_parser("check", help="Check problem folders and local tests")
    p.set_defaults(func=check_project)

    p = sub.add_parser("list", help="List problems")
    p.add_argument("--category")
    p.add_argument("--difficulty")
    p.set_defaults(func=list_problems)

    p = sub.add_parser("run", help="Run local tests for one problem")
    p.add_argument("slug")
    p.add_argument("--file", help="Use a custom solution file")
    p.add_argument("--case", type=int, help="Run only one 1-based test case")
    p.add_argument("--all", action="store_true", help="Keep running after failures")
    p.add_argument("--debug", action="store_true", help="Show print() output from your solution")
    p.set_defaults(func=run_problem)

    p = sub.add_parser("show", help="Show a problem summary")
    p.add_argument("slug")
    p.set_defaults(func=show_problem)

    p = sub.add_parser("status", help="Show progress")
    p.set_defaults(func=show_status)

    args = parser.parse_args()
    result = args.func(args)
    if isinstance(result, int):
        raise SystemExit(result)


if __name__ == "__main__":
    main()
