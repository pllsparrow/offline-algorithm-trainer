import json
import unittest

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
        for slug in problems:
            path = train.solution_path(slug)
            self.assertEqual("solution.py", path.name, slug)
            self.assertTrue(path.is_file(), slug)
            self.assertEqual("", specs[slug]["starter"], slug)

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
        self.assertEqual(18, len(result["results"]))

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
