import json
import shutil
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from web_app import ApiError, AppService


ROOT = Path(__file__).resolve().parents[1]


class WebAppTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        (self.root / "data").mkdir()
        (self.root / "hot_150").mkdir()
        problem = {
            "index": 1,
            "slug": "sample-sum",
            "title": "Sample Sum",
            "difficulty": "Easy",
            "category": "Basics",
            "summary": "Add two integers.",
            "practice_url": "https://example.com/sample-sum",
            "path": "hot_150/q001_sample_sum.py",
        }
        spec = {
            "protocol": "text",
            "format": "Input: two integers. Output: their sum.",
            "cases": [
                {"stdin": "1 2\n", "stdout": "3\n"},
                {"stdin": "-5 8\n", "stdout": "3\n"},
            ],
        }
        examples = {
            "sample-sum": [
                {"name": "Positive", "stdin": "1 2\n", "stdout": "3\n", "reason": "Basic addition."}
            ]
        }
        (self.root / "data" / "problems.json").write_text(json.dumps([problem]), encoding="utf-8")
        (self.root / "data" / "acm_tests.json").write_text(json.dumps({"sample-sum": spec}), encoding="utf-8")
        (self.root / "data" / "examples.json").write_text(json.dumps(examples), encoding="utf-8")
        self.solution = self.root / problem["path"]
        self.solution.write_text("# starter\n", encoding="utf-8")
        shutil.copy(ROOT / "web_debug_runner.py", self.root / "web_debug_runner.py")
        self.app = AppService(self.root, self.root / "data" / "progress.sqlite3")

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_problem_detail_and_draft_persistence(self) -> None:
        self.assertEqual(1, len(self.app.list_problems()))
        detail = self.app.get_problem(1)
        self.assertEqual("# starter\n", detail["source"])
        self.assertEqual("1 2\n", detail["examples"][0]["stdin"])

        self.app.save_draft(1, "print('draft')\n")

        self.assertEqual("print('draft')\n", self.app.get_problem(1)["draft_source"])
        self.assertEqual("# starter\n", self.solution.read_text(encoding="utf-8"))

    def test_custom_run_returns_structured_runtime_error(self) -> None:
        result = self.app.run({"index": 1, "source": "values = []\nprint(values[1])\n", "stdin": ""})

        self.assertFalse(result["ok"])
        self.assertEqual("IndexError", result["error"]["type"])
        self.assertEqual(2, result["error"]["line"])
        self.assertTrue(result["error"]["hint"])

    def test_custom_run_bounds_captured_output(self) -> None:
        result = self.app.run({"index": 1, "source": "print('x' * 100000)\n", "stdin": ""})

        self.assertLessEqual(len(result["stdout"].encode("utf-8")), 65_536)

    def test_submit_runs_all_cases_writes_source_and_records_progress(self) -> None:
        source = "a, b = map(int, input().split())\nprint(a + b)\n"

        result = self.app.submit({"index": 1, "source": source})

        self.assertTrue(result["ok"])
        self.assertEqual((2, 2), (result["passed"], result["total"]))
        self.assertEqual(source, self.solution.read_text(encoding="utf-8"))
        self.assertEqual("accepted", self.app.list_problems()[0]["progress"])
        self.assertTrue(result["saved"])
        self.assertEqual("hot_150/q001_sample_sum.py", result["saved_path"])

    def test_submit_saves_source_before_case_execution(self) -> None:
        source = "print('saved before tests')\n"

        with patch("web_app.execute", side_effect=RuntimeError("runner unavailable")):
            with self.assertRaisesRegex(RuntimeError, "runner unavailable"):
                self.app.submit({"index": 1, "source": source})

        self.assertEqual(source, self.solution.read_text(encoding="utf-8"))

    def test_debug_session_pauses_steps_and_finishes(self) -> None:
        source = "value = 1\nvalue += 2\nprint(value)\n"

        session_id, paused = self.app.debugger.start(source, "", [2])
        stepped = self.app.debugger.command(session_id, "step", [2])
        finished = self.app.debugger.command(session_id, "continue", [2])

        self.assertEqual(("paused", 2), (paused["state"], paused["line"]))
        self.assertEqual(("paused", 3), (stepped["state"], stepped["line"]))
        self.assertEqual("finished", finished["state"])
        self.assertEqual("3\n", finished["stdout"])

    def test_invalid_problem_and_oversized_source_are_rejected(self) -> None:
        with self.assertRaises(ApiError):
            self.app.get_problem(999)
        with self.assertRaises(ApiError):
            self.app.save_draft(1, "x" * 300_000)


class MaterializedExamplesTests(unittest.TestCase):
    def test_every_problem_has_two_or_three_unique_examples(self) -> None:
        problems = json.loads((ROOT / "data" / "problems.json").read_text(encoding="utf-8"))
        examples = json.loads((ROOT / "data" / "examples.json").read_text(encoding="utf-8"))

        self.assertEqual({problem["slug"] for problem in problems}, set(examples))
        for slug, items in examples.items():
            self.assertGreaterEqual(len(items), 2, slug)
            self.assertLessEqual(len(items), 3, slug)
            self.assertEqual(len(items), len({item["stdin"] for item in items}), slug)
            for item in items:
                self.assertTrue(item["name"], slug)
                self.assertTrue(item["reason"], slug)
                self.assertNotRegex(item["name"] + item["reason"], r"[\u4e00-\u9fff]", slug)
                self.assertIn("stdout", item, slug)
                self.assertFalse(item["name"].startswith("Example "), slug)
                self.assertNotIn("representative example", item["reason"].lower(), slug)

    def test_web_shell_has_collapsible_navigation_without_difficulty_filter(self) -> None:
        html = (ROOT / "web" / "index.html").read_text(encoding="utf-8")

        self.assertIn('id="toggle-sidebar"', html)
        self.assertIn('class="sidebar-toggle-icon"', html)
        self.assertIn('aria-label="Collapse problem library"', html)
        self.assertNotIn("<header>", html)
        self.assertIn("color-scheme: light", html)
        self.assertIn('id="previous-problem"', html)
        self.assertIn('id="next-problem"', html)
        self.assertIn("width: 10px; height: 10px", html)
        self.assertIn('.cm-breakpoint-gutter { background: #f2eedf !important; cursor: pointer; }', html)
        self.assertIn("const LAST_PROBLEM_KEY = 'last-problem-index'", html)
        self.assertIn("localStorage.setItem(LAST_PROBLEM_KEY", html)
        self.assertIn('id="jump"', html)
        self.assertIn('id="search"', html)
        self.assertNotIn('id="difficulty"', html)
        self.assertNotIn('id="source"', html)
        self.assertIn('/assets/editor.bundle.js', html)
        self.assertIn("expected stdout", html)
        self.assertIn("Load input", html)
        self.assertIn("Run case", html)
        self.assertIn("data-example-stdin", html)
        self.assertNotRegex(html, r"[\u4e00-\u9fff]")

        editor_source = (ROOT / "web" / "editor.js").read_text(encoding="utf-8")
        self.assertIn("closeBrackets()", editor_source)
        self.assertIn("bracketMatching()", editor_source)
        self.assertIn("spellingCheck", editor_source)
        self.assertIn('class: "cm-spelling-error"', editor_source)
        self.assertNotIn("autocompletion()", editor_source)


if __name__ == "__main__":
    unittest.main()
