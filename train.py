#!/usr/bin/env python3
"""Offline algorithm training CLI (ACM stdin/stdout mode only).

Every problem is an ACM-style program that reads stdin and writes stdout.
The judge runs each solution as an independent Python process, feeds it the
test-case stdin, captures stdout, and compares it (whitespace-normalised)
against the expected output.
"""
import argparse
import json
import sqlite3
import subprocess
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
QUESTIONS_DIR = ROOT / "questions"
DB = DATA / "progress.sqlite3"


def load_json(path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def problems_by_slug():
    return {p["slug"]: p for p in load_json(DATA / "problems.json")}


def specs_by_slug():
    return load_json(DATA / "acm_tests.json")


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
        return ROOT / problem["path"]
    return QUESTIONS_DIR / f"{slug.replace('-', '_')}.py"


def resolve_slug(reference=None, file_path=None):
    problems = problems_by_slug()
    if reference:
        if reference in problems:
            return reference
        number = reference.split("-", 1)[0]
        if number.isdigit():
            index = int(number)
            for slug, problem in problems.items():
                if problem["index"] == index:
                    return slug
        return None
    if file_path:
        candidate = Path(file_path).resolve()
        for slug in problems:
            if solution_path(slug).resolve() == candidate:
                return slug
    return None


def starter_with_io_comments(spec):
    format_text = spec.get("format", "").strip()
    input_text, separator, output_text = format_text.partition(" Output: ")
    if input_text.startswith("Input: "):
        input_text = input_text.removeprefix("Input: ")
    if not separator:
        output_text = "see the problem specification"
    return f"# Input: {input_text}\n# Output: {output_text}\n\n"


def scaffold(args):
    problems = problems_by_slug()
    specs = specs_by_slug()
    QUESTIONS_DIR.mkdir(exist_ok=True)
    files_created = 0
    for slug, problem in problems.items():
        spec = specs.get(slug, {"cases": []})
        path = solution_path(slug)
        if not path.exists() or args.force:
            path.write_text(starter_with_io_comments(spec), encoding="utf-8")
            files_created += 1
    print(f"Scaffold ready: {len(problems)} problems, {files_created} question files.")
    print(f"Open this folder in PyCharm: {ROOT}")


def check_project(args):
    problems = problems_by_slug()
    specs = specs_by_slug()
    issues = []
    exhaustive_case_counts = {
        "generate-parentheses": 9,
        "n-queens": 10,
    }
    extra_specs = sorted(set(specs) - set(problems))
    for slug in extra_specs:
        issues.append(f"{slug}: ACM spec has no matching problem")
    for slug, problem in problems.items():
        if slug not in specs:
            issues.append(f"{slug}: missing ACM spec in data/acm_tests.json")
        else:
            spec = specs[slug]
            if spec.get("protocol") != "text":
                issues.append(f"{slug}: ACM protocol must be text")
            cases = spec.get("cases")
            if not cases:
                issues.append(f"{slug}: ACM spec has no test cases")
            elif any("stdin" not in case or "stdout" not in case for case in cases):
                issues.append(f"{slug}: every ACM case must define stdin and stdout")
            else:
                expected_count = exhaustive_case_counts.get(slug)
                if expected_count is not None and len(cases) != expected_count:
                    issues.append(f"{slug}: expected {expected_count} exhaustive ACM cases")
                elif expected_count is None and not 46 <= len(cases) <= 55:
                    issues.append(f"{slug}: expected 46 to 55 ACM cases")
                inputs = [case["stdin"] for case in cases]
                if len(inputs) != len(set(inputs)):
                    issues.append(f"{slug}: ACM cases contain duplicate stdin")
        path = solution_path(slug)
        if not path.is_file():
            issues.append(f"{slug}: missing question file {path}")
    if issues:
        print(f"Project check failed: {len(issues)} issue(s)")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print(f"Project check passed: {len(problems)} problems, {len(specs)} ACM specs")
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


def run_acm_judge(slug, code, *, case=None, run_all=False):
    specs = specs_by_slug()
    if slug not in specs:
        return {"ok": False, "error": "No ACM test spec for this problem yet."}
    proc = subprocess.run(
        [sys.executable, str(ROOT / "judge" / "acm_judge.py")],
        input=json.dumps(
            {
                "slug": slug,
                "code": code,
                "cases": specs[slug]["cases"],
                "case": case,
                "run_all": run_all,
            },
            ensure_ascii=False,
        ),
        text=True,
        capture_output=True,
        timeout=12,
    )
    if proc.returncode != 0:
        return {"ok": False, "error": proc.stderr.strip() or proc.stdout.strip() or "ACM judge failed"}
    try:
        return json.loads(proc.stdout)
    except json.JSONDecodeError:
        return {"ok": False, "error": "ACM judge returned invalid JSON", "trace": proc.stdout}


def short_repr(value, limit=220):
    text = repr(value)
    if len(text) <= limit:
        return text
    return text[: limit - 3] + "..."


def print_case_detail(item):
    print(f"Case {item['case']}: fail")
    case_input = item.get("input", {})
    print(f"  stdin:    {short_repr(case_input.get('stdin', ''))}")
    print(f"  expected: {short_repr(item['expected'])}")
    print(f"  actual:   {short_repr(item['actual'])}")
    if item.get("actual") and "process exited" not in item["actual"]:
        print("  actual (raw):")
        for line in item["actual"].rstrip().splitlines():
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
            continue
        print_case_detail(item)
        if result.get("selected_case") is None:
            print()
            print(
                f"Repeat this case: python3 train.py run {result['slug']} "
                f"--case {item['case']}"
            )
        if not show_all_failures:
            break


def run_problem(args):
    problems = problems_by_slug()
    slug = resolve_slug(args.slug, args.file)
    if slug is None:
        reference = args.slug or args.file or "<missing>"
        print(f"Unknown problem: {reference}", file=sys.stderr)
        return 2
    specs = specs_by_slug()
    if slug not in specs:
        print(f"No ACM test spec for {slug} yet", file=sys.stderr)
        return 2
    if args.case is not None and not 1 <= args.case <= len(specs[slug]["cases"]):
        print(f"--case must be between 1 and {len(specs[slug]['cases'])}", file=sys.stderr)
        return 2
    path = Path(args.file) if args.file else solution_path(slug)
    if not path.exists():
        print(f"Missing solution file: {path}", file=sys.stderr)
        print(f"Run: python3 train.py scaffold", file=sys.stderr)
        return 2
    result = run_acm_judge(
        slug,
        path.read_text(encoding="utf-8"),
        case=args.case,
        run_all=args.all,
    )
    update_progress(slug, path.read_text(encoding="utf-8"), result)
    print_result(result, show_passed=args.all, show_all_failures=args.all)
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
    slug = resolve_slug(args.slug)
    problem = problems.get(slug)
    if not problem:
        print(f"Unknown problem: {args.slug}", file=sys.stderr)
        return 2
    spec = specs_by_slug().get(slug)
    if not spec:
        print(f"No ACM test spec for {slug}", file=sys.stderr)
        return 2
    print(f"{problem['title']} [{problem['difficulty']}] - ACM")
    print(problem["category"])
    print()
    print(f"Format: {spec['format']}")
    print()
    for index, case in enumerate(spec["cases"][:3], start=1):
        print(f"Case {index} stdin:")
        print(case["stdin"], end="" if case["stdin"].endswith("\n") else "\n")
        print(f"Expected: {case['stdout']!r}")
        print()
    print(f"File: {solution_path(slug)}")
    return 0


def main():
    parser = argparse.ArgumentParser(description="Offline algorithm training CLI (ACM mode)")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("scaffold", help="Create problem folders, READMEs, and empty solution files")
    p.add_argument("--force", action="store_true", help="Overwrite READMEs and empty all solution files")
    p.set_defaults(func=scaffold)

    p = sub.add_parser("check", help="Check problem folders and ACM specs")
    p.set_defaults(func=check_project)

    p = sub.add_parser("list", help="List problems")
    p.add_argument("--category")
    p.add_argument("--difficulty")
    p.set_defaults(func=list_problems)

    p = sub.add_parser("run", help="Run local ACM tests for one problem")
    p.add_argument("slug", nargs="?", help="Problem slug or number; omit when using --file")
    p.add_argument("--file", help="Use a custom solution file")
    p.add_argument("--case", type=int, help="Run only one 1-based test case")
    p.add_argument("--all", action="store_true", help="Keep running after failures")
    p.set_defaults(func=run_problem)

    p = sub.add_parser("show", help="Show a problem summary and ACM format")
    p.add_argument("slug", help="Problem slug or number")
    p.set_defaults(func=show_problem)

    p = sub.add_parser("status", help="Show progress")
    p.set_defaults(func=show_status)

    args = parser.parse_args()
    result = args.func(args)
    if isinstance(result, int):
        raise SystemExit(result)


if __name__ == "__main__":
    main()
