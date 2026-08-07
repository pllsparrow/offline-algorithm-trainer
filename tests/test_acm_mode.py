import json
import unittest
from pathlib import Path

import acm_support
import train


ROOT = Path(__file__).resolve().parents[1]


class AcmModeTests(unittest.TestCase):
    def test_all_problems_have_specs_and_starters(self) -> None:
        problems = train.problems_by_slug()
        specs = train.acm_tests_by_slug()

        self.assertEqual(150, len(problems))
        self.assertEqual(set(problems), set(specs))
        self.assertEqual(8, sum(spec["protocol"] == "text" for spec in specs.values()))
        self.assertEqual(142, sum(spec["protocol"] == "json" for spec in specs.values()))
        for slug in problems:
            self.assertTrue(train.acm_solution_path(slug).is_file(), slug)

    def test_every_starter_compiles(self) -> None:
        for slug in train.problems_by_slug():
            path = train.acm_solution_path(slug)
            compile(path.read_text(encoding="utf-8"), str(path), "exec")

    def test_tree_and_linked_list_round_trip(self) -> None:
        tree = acm_support.list_to_tree([3, 9, 20, None, None, 15, 7])
        linked = acm_support.list_to_linked([1, 2, 3])

        self.assertEqual([3, 9, 20, None, None, 15, 7], acm_support.normalize(tree))
        self.assertEqual([1, 2, 3], acm_support.normalize(linked))

    def test_operation_names_map_to_python_style(self) -> None:
        self.assertEqual("get_min", acm_support.camel_to_snake("getMin"))
        self.assertEqual("get_news_feed", acm_support.camel_to_snake("getNewsFeed"))

    def test_json_protocol_runs_in_an_independent_process(self) -> None:
        code = """
from acm_support import run_solution

class Solution:
    def is_anagram(self, left, right):
        return sorted(left) == sorted(right)

if __name__ == "__main__":
    run_solution(Solution, "is_anagram", ["", ""])
"""
        result = train.run_acm_judge("valid-anagram", code, run_all=True)

        self.assertTrue(result["ok"], json.dumps(result, ensure_ascii=False))
        self.assertEqual(18, len(result["results"]))


if __name__ == "__main__":
    unittest.main()
