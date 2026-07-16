#!/usr/bin/env python3
from __future__ import annotations

import ast
import json
import re
import shutil
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
PROBLEMS = ROOT / "problems"
REFERENCE = Path("/tmp/leetcode-py/leetcode")
ROADMAP_URL = "https://raw.githubusercontent.com/krmanik/Anki-NeetCode/main/neetcode-150-list.json"

CHAPTER_SLUGS = {
    "Arrays & Hashing": "arrays-hashing",
    "Two Pointers": "two-pointers",
    "Sliding Window": "sliding-window",
    "Stack": "stack",
    "Binary Search": "binary-search",
    "Linked List": "linked-list",
    "Trees": "trees",
    "Heap / Priority Queue": "heap-priority-queue",
    "Backtracking": "backtracking",
    "Tries": "tries",
    "Graphs": "graphs",
    "Advanced Graphs": "advanced-graphs",
    "1-D Dynamic Programming": "1d-dynamic-programming",
    "2-D Dynamic Programming": "2d-dynamic-programming",
    "Greedy": "greedy",
    "Intervals": "intervals",
    "Math & Geometry": "math-geometry",
    "Bit Manipulation": "bit-manipulation",
}

FOCUS = {
    "Arrays & Hashing": ["hash table modeling", "frequency counting", "single-pass array traversal", "deduplication and index mapping"],
    "Two Pointers": ["left/right pointers", "sorted array scanning", "range shrinking", "duplicate handling"],
    "Sliding Window": ["window invariants", "left/right boundary movement", "frequency table maintenance", "shortest/longest substring patterns"],
    "Stack": ["monotonic stacks", "parentheses matching", "expression evaluation", "auxiliary state maintenance"],
    "Binary Search": ["search space definition", "boundary shrinking", "binary search on the answer", "rotated array decisions"],
    "Linked List": ["pointer rewiring", "fast and slow pointers", "dummy head nodes", "in-place list mutation"],
    "Trees": ["recursive return-value design", "DFS/BFS", "BST properties", "tree DP"],
    "Heap / Priority Queue": ["Top K", "two heaps", "task scheduling", "lazy deletion versus sorting tradeoffs"],
    "Backtracking": ["choice paths", "pruning", "duplicate handling", "state restoration"],
    "Tries": ["trie node design", "string search", "DFS plus trie pruning"],
    "Graphs": ["DFS/BFS", "topological sorting", "union find", "graph modeling"],
    "Advanced Graphs": ["shortest paths", "minimum spanning trees", "Eulerian paths", "constrained graph search"],
    "1-D Dynamic Programming": ["state definition", "transition equations", "rolling variables", "knapsack models"],
    "2-D Dynamic Programming": ["2D state design", "string DP", "interval DP", "path DP"],
    "Greedy": ["local optimality proofs", "interval/jump strategies", "counterexample awareness", "single-pass scans"],
    "Intervals": ["sorting then merging", "overlap checks", "sweep lines", "heap-based meeting room tracking"],
    "Math & Geometry": ["in-place matrix operations", "simulation", "mathematical boundaries", "coordinate hashing"],
    "Bit Manipulation": ["bit manipulation tricks", "XOR properties", "two's-complement boundaries", "bit-by-bit construction"],
}

SUMMARIES = {
    "two-sum": "Find the indices of two numbers whose sum equals the target. Practice looking up complements while traversing with a hash table.",
    "contains-duplicate": "Determine whether an array contains any duplicate value. This is a starter problem for set-based deduplication.",
    "valid-anagram": "Determine whether two strings contain the same characters with the same counts. Practice character frequency counting.",
    "group-anagrams": "Group strings that are anagrams of each other. Practice turning a complex object into a stable grouping key.",
    "top-k-frequent-elements": "Return the k most frequent elements. Practice frequency counting, heaps, and bucket-style thinking.",
    "valid-palindrome": "Check whether a string is a palindrome after ignoring case and non-alphanumeric characters. Practice two-pointer scanning.",
    "min-stack": "Design a stack that can return the minimum value in O(1). Practice maintaining auxiliary stack state.",
    "binary-search": "Search for a target in a sorted array. Practice binary-search boundaries.",
    "reverse-linked-list": "Reverse a singly linked list. Practice fundamental pointer rewiring.",
    "invert-binary-tree": "Invert a binary tree. Practice recursively processing left and right subtrees.",
    "number-of-islands": "Count islands in a grid. Practice DFS/BFS flood fill.",
    "climbing-stairs": "Count the ways to reach the nth stair when you can climb 1 or 2 steps at a time. Practice 1D DP.",
    "coin-change": "Find the minimum number of coins needed to make a target amount. Practice complete-knapsack DP.",
    "maximum-subarray": "Find the maximum sum of a contiguous subarray. Practice Kadane's algorithm and local state transitions.",
}


def slug_to_reference_name(slug: str) -> str:
    aliases = {"3sum": "three_sum"}
    if slug in aliases:
        return aliases[slug]
    return slug.replace("-", "_")


def get_roadmap() -> dict:
    with urllib.request.urlopen(ROADMAP_URL, timeout=20) as response:
        return json.load(response)


def title_slug(url: str, title: str) -> str:
    slug = url.rstrip("/").split("/")[-1]
    if slug:
        return slug
    return re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")


def literal_parametrize(test_file: Path) -> tuple[list[str], list[list]] | None:
    class PytestShim:
        @staticmethod
        def param(*args, **kwargs):
            return args

    tree = ast.parse(test_file.read_text(encoding="utf-8"))
    for node in ast.walk(tree):
        if not isinstance(node, ast.FunctionDef):
            continue
        for decorator in node.decorator_list:
            if not isinstance(decorator, ast.Call) or len(decorator.args) < 2:
                continue
            src = ast.unparse(decorator.func)
            if not src.endswith("pytest.mark.parametrize"):
                continue
            names = ast.literal_eval(decorator.args[0])
            if isinstance(names, str):
                names = [name.strip() for name in names.split(",")]
            try:
                cases = ast.literal_eval(decorator.args[1])
            except Exception:
                safe_globals = {"__builtins__": {}}
                safe_locals = {
                    "inf": float("inf"),
                    "float": float,
                    "Solution": "__Solution__",
                    "pytest": PytestShim,
                }
                cases = eval(compile(ast.Expression(decorator.args[1]), str(test_file), "eval"), safe_globals, safe_locals)
            if names and names[0] == "solution_class":
                names = names[1:]
                cases = [case[1:] for case in cases]
            return names, [list(case) if isinstance(case, tuple) else [case] for case in cases]
    return None


def class_and_methods(solution_file: Path) -> tuple[str, list[str]]:
    tree = ast.parse(solution_file.read_text(encoding="utf-8"))
    classes = [node for node in tree.body if isinstance(node, ast.ClassDef)]
    primary = next((node for node in classes if node.name not in {"SolutionDFS", "SolutionBFS"}), None)
    if primary is None:
        return "Solution", ["solve"]
    methods = [node.name for node in primary.body if isinstance(node, ast.FunctionDef)]
    return primary.name, methods


def make_stub(solution_file: Path, class_name: str, methods: list[str]) -> str:
    tree = ast.parse(solution_file.read_text(encoding="utf-8"))
    cls = next((node for node in tree.body if isinstance(node, ast.ClassDef) and node.name == class_name), None)
    lines = ["from __future__ import annotations", "", "from support import GraphNode, ListNode, Node, RandomNode, TreeNode", "", ""]
    if cls is None:
        lines += ["class Solution:", "    def solve(self):", "        pass", ""]
        return "\n".join(lines)
    lines.append(f"class {class_name}:")
    has_method = False
    for item in cls.body:
        if not isinstance(item, ast.FunctionDef):
            continue
        has_method = True
        for decorator in item.decorator_list:
            lines.append(f"    @{ast.unparse(decorator)}")
        returns = f" -> {ast.unparse(item.returns)}" if item.returns else ""
        signature = f"def {item.name}({ast.unparse(item.args)}){returns}:"
        lines.append(f"    {signature}")
        lines.append("        pass")
        lines.append("")
    if not has_method:
        lines.append("    pass")
    return "\n".join(lines).rstrip() + "\n"


def infer_param_type(slug: str, name: str) -> str:
    if name in {"head_list", "list1_data", "list2_data"}:
        return "ListNode"
    if name == "lists_data":
        return "List[ListNode]"
    if name in {"root_list", "p_list", "q_list", "sub_root_list"}:
        return "TreeNode"
    if name in {"p_val", "q_val"} and "lowest-common-ancestor" in slug:
        return "TreeNodeValue"
    if name == "adj_list":
        return "GraphNode"
    if slug == "copy-list-with-random-pointer" and name == "nodes":
        return "RandomNode"
    return ""


def jsonable(value):
    if isinstance(value, set):
        return sorted(jsonable(item) for item in value)
    if isinstance(value, tuple):
        return [jsonable(item) for item in value]
    if isinstance(value, list):
        return [jsonable(item) for item in value]
    if isinstance(value, dict):
        return {key: jsonable(item) for key, item in value.items()}
    return value


def build_tests(slug: str, ref_dir: Path, class_name: str, methods: list[str]) -> dict | None:
    test_file = ref_dir / "test_solution.py"
    if not test_file.exists():
        return None
    parsed = literal_parametrize(test_file)
    if not parsed:
        return None
    names, rows = parsed
    if names[:2] == ["operations", "inputs"]:
        return {
            "method": "__ops__",
            "class": rows[0][0][0] if rows and rows[0] else class_name,
            "cases": [{"ops": jsonable(row[0]), "args": jsonable(row[1]), "expected": jsonable(row[2])} for row in rows],
        }
    expected_index = next((i for i, name in enumerate(names) if name.startswith("expected")), None)
    if expected_index is None:
        # Clone Graph style: expected is the input itself.
        expected_index = len(names)
    arg_names = names[:expected_index]
    method = next((name for name in methods if name != "__init__"), "solve")
    cases = []
    for row in rows:
        args = row[:expected_index]
        expected = row[expected_index] if expected_index < len(row) else row[0]
        cases.append({"args": jsonable(args), "expected": jsonable(expected)})
    if slug == "n-queens":
        existing = {tuple(case["args"]) for case in cases}
        for n, count in [(7, 40), (8, 92), (9, 352), (10, 724)]:
            if (n,) not in existing:
                cases.append(
                    {
                        "args": [n],
                        "expected": {"valid_solution_count": count},
                        "expected_count": count,
                    }
                )
    return {
        "method": method,
        "param_types": [infer_param_type(slug, name) for name in arg_names],
        "cases": cases,
    }


def render_problem_readme(problem: dict, test_spec: dict | None) -> str:
    examples = "Local tests have not been added yet."
    if test_spec:
        blocks = []
        for idx, case in enumerate(test_spec.get("cases", [])[:5], start=1):
            if "ops" in case:
                body = f"ops = {case['ops']!r}\nargs = {case['args']!r}\nexpected = {case['expected']!r}"
            else:
                body = f"args = {case['args']!r}\nexpected = {case['expected']!r}"
            blocks.append(f"### Case {idx}\n\n```python\n{body}\n```")
        examples = "\n\n".join(blocks)
    hints = "\n".join(f"- {hint}" for hint in problem["hints"])
    return f"""# {problem['index']:03d}. {problem['title']}

- Chapter: {problem['chapter']:02d}. {problem['category']}
- Difficulty: {problem['difficulty']}
- Source: {problem['source_url']}
- Reference: {problem['practice_url']}

## Goal

{problem['summary']}

## Interview Focus

{hints}

## Local Examples

{examples}

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run {problem['slug']}
```
"""


def main() -> None:
    if not REFERENCE.exists():
        raise SystemExit("Missing /tmp/leetcode-py. Clone wislertt/leetcode-py there first.")
    DATA.mkdir(exist_ok=True)
    if PROBLEMS.exists():
        shutil.rmtree(PROBLEMS)
    PROBLEMS.mkdir()

    roadmap = get_roadmap()
    problems = []
    tests = {}
    index = 0

    for chapter, (category, items) in enumerate(roadmap.items(), start=1):
        chapter_dir = PROBLEMS / f"{chapter:02d}-{CHAPTER_SLUGS[category]}"
        chapter_dir.mkdir()
        chapter_lines = [f"# {chapter:02d}. {category}", "", "## Focus", ""]
        chapter_lines.extend(f"- {item}" for item in FOCUS[category])
        chapter_lines.extend(["", "## Problems", ""])

        for title, meta in items.items():
            index += 1
            slug = title_slug(meta.get("url", ""), title)
            ref_dir = REFERENCE / slug_to_reference_name(slug)
            solution_file = ref_dir / "solution.py"
            class_name, methods = class_and_methods(solution_file) if solution_file.exists() else ("Solution", ["solve"])
            test_spec = build_tests(slug, ref_dir, class_name, methods)
            if test_spec:
                tests[slug] = test_spec
            folder = chapter_dir / f"{index:03d}-{slug}"
            folder.mkdir()
            starter = make_stub(solution_file, class_name, methods) if solution_file.exists() else "class Solution:\n    def solve(self):\n        pass\n"
            focus = FOCUS[category]
            problem = {
                "index": index,
                "slug": slug,
                "title": title,
                "category": category,
                "chapter": chapter,
                "difficulty": meta["difficulty"],
                "method": test_spec.get("method", methods[0]) if test_spec else methods[0],
                "summary": SUMMARIES.get(slug, f"Classic interview problem for {title}. Practice {focus[0]} and {focus[1]}. Start with a brute-force idea, then optimize to an interview-ready complexity."),
                "signature": " / ".join(methods),
                "starter": starter,
                "hints": [
                    f"Identify the core pattern: {focus[0]}.",
                    f"Before coding, state the invariant or state definition: {focus[1]}.",
                    "After it passes, explain the time complexity, space complexity, and one edge case.",
                ],
                "source_url": meta.get("url", ""),
                "practice_url": meta.get("nurl", ""),
                "path": str(folder.relative_to(ROOT)),
            }
            problems.append(problem)
            (folder / "README.md").write_text(render_problem_readme(problem, test_spec), encoding="utf-8")
            (folder / "solution.py").write_text(starter, encoding="utf-8")
            chapter_lines.append(f"- [{index:03d}. {title}]({index:03d}-{slug}/README.md) `{meta['difficulty']}`")

        (chapter_dir / "README.md").write_text("\n".join(chapter_lines) + "\n", encoding="utf-8")

    (DATA / "problems.json").write_text(json.dumps(problems, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (DATA / "tests.json").write_text(json.dumps(tests, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Generated {len(problems)} problems in {len(roadmap)} chapters.")
    print(f"Generated local tests for {len(tests)} problems.")


if __name__ == "__main__":
    main()
