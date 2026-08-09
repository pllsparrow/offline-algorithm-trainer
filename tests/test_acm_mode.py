import json
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

import train


class AcmModeTests(unittest.TestCase):
    def test_problem_references_accept_slugs_numbers_and_solution_paths(self) -> None:
        first_path = train.solution_path("contains-duplicate")

        self.assertEqual("contains-duplicate", train.resolve_slug("contains-duplicate"))
        self.assertEqual("contains-duplicate", train.resolve_slug("001"))
        self.assertEqual("contains-duplicate", train.resolve_slug("1"))
        self.assertEqual("two-sum", train.resolve_slug("003-two-sum"))
        self.assertEqual("contains-duplicate", train.resolve_slug(file_path=first_path))
        self.assertIsNone(train.resolve_slug("999"))
        for slug in train.problems_by_slug():
            self.assertEqual(slug, train.resolve_slug(file_path=train.solution_path(slug)))

    def test_all_problems_have_specs_and_blank_starters(self) -> None:
        problems = train.problems_by_slug()
        specs = train.specs_by_slug()

        self.assertEqual(150, len(problems))
        self.assertEqual(set(problems), set(specs))
        self.assertTrue(all(spec["protocol"] == "text" for spec in specs.values()))
        for slug, problem in problems.items():
            path = train.solution_path(slug)
            expected_name = f"q{problem['index']:03d}_{slug.replace('-', '_')}.py"
            self.assertEqual(expected_name, path.name, slug)
            self.assertEqual("questions", path.parent.name, slug)
            self.assertTrue(path.is_file(), slug)
            self.assertEqual("", specs[slug]["starter"], slug)

    def test_every_problem_has_runnable_acm_cases(self) -> None:
        exhaustive_domains = {
            "generate-parentheses": 9,
            "n-queens": 10,
        }
        for slug, spec in train.specs_by_slug().items():
            self.assertEqual("text", spec.get("protocol"), slug)
            self.assertTrue(spec.get("cases"), slug)
            if slug in exhaustive_domains:
                self.assertEqual(exhaustive_domains[slug], len(spec["cases"]), slug)
            else:
                self.assertGreaterEqual(len(spec["cases"]), 46, slug)
                self.assertLessEqual(len(spec["cases"]), 55, slug)
            inputs = [case["stdin"] for case in spec["cases"]]
            self.assertEqual(len(inputs), len(set(inputs)), slug)
            for case in spec["cases"]:
                self.assertIn("stdin", case, slug)
                self.assertIn("stdout", case, slug)

    def test_shared_run_configuration_judges_the_current_file(self) -> None:
        config_path = Path(".run/Judge Current Solution.run.xml")
        configuration = ET.parse(config_path).getroot().find("configuration")
        self.assertIsNotNone(configuration)

        options = {
            option.get("name"): option.get("value")
            for option in configuration.findall("option")
        }
        self.assertEqual("$PROJECT_DIR$/train.py", options.get("SCRIPT_NAME"))
        self.assertEqual('run --file "$FilePath$"', options.get("PARAMETERS"))

    def test_every_solution_compiles(self) -> None:
        for slug in train.problems_by_slug():
            path = train.solution_path(slug)
            code = path.read_text(encoding="utf-8")
            compile(code, str(path), "exec")

    def test_text_protocol_runs_in_an_independent_process(self) -> None:
        code = """
import sys


def main():
    input_stream = sys.stdin.buffer
    left = input_stream.readline().strip()
    right = input_stream.readline().strip()
    print(1 if sorted(left) == sorted(right) else 0)

if __name__ == "__main__":
    main()
"""
        result = train.run_acm_judge("valid-anagram", code, run_all=True)

        self.assertTrue(result["ok"], json.dumps(result, ensure_ascii=False))
        self.assertEqual(50, len(result["results"]))

    def test_length_prefixed_strings_use_utf8_byte_lengths(self) -> None:
        code = """
import sys


def main():
    input_stream = sys.stdin.buffer
    string_count = int(input_stream.readline())
    output = [str(string_count).encode()]
    for _ in range(string_count):
        byte_count = int(input_stream.readline())
        value = input_stream.read(byte_count)
        input_stream.read(1)
        output.extend((str(byte_count).encode(), value))
    sys.stdout.buffer.write(b"\\n".join(output) + b"\\n")


if __name__ == "__main__":
    main()
"""
        result = train.run_acm_judge("encode-and-decode-strings", code, run_all=True)

        self.assertTrue(result["ok"], json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    unittest.main()
