import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOPIC = ROOT / "muscle_memory" / "heapq&buckets"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


sys.path.insert(0, str(TOPIC))
case_generators = load_module("heap_bucket_cases", TOPIC / "case_generators.py")
judge = load_module("heap_bucket_judge", TOPIC / "judge.py")


class HeapBucketExerciseTests(unittest.TestCase):
    def test_each_exercise_has_99_unique_cases(self) -> None:
        self.assertEqual(15, len(case_generators.EXERCISES))
        for exercise_id in case_generators.EXERCISES:
            cases = case_generators.build_cases(exercise_id)
            self.assertEqual(99, len(cases), exercise_id)
            self.assertEqual(99, len({case.stdin for case in cases}), exercise_id)

    def test_each_exercise_has_at_least_90_substantial_cases(self) -> None:
        for exercise_id in case_generators.EXERCISES:
            cases = case_generators.build_cases(exercise_id)
            substantial = sum(case.size >= 100 for case in cases)
            self.assertGreaterEqual(substantial, 90, exercise_id)

    def test_canonical_expected_outputs_pass_every_validator(self) -> None:
        for exercise_id in case_generators.EXERCISES:
            for case in case_generators.build_cases(exercise_id):
                self.assertTrue(judge.output_matches(exercise_id, case, case.expected), exercise_id)

    def test_semantic_validators_accept_distinct_valid_answers(self) -> None:
        pairs = case_generators.Case("2 2 2\n1 2\n1 2\n", "1 1\n1 2\n", 4, "tie")
        self.assertTrue(judge.output_matches("h02", pairs, "1 1\n2 1\n"))

        reorganize = case_generators.Case("aabb\n", "abab\n", 4, "tie")
        self.assertTrue(judge.output_matches("h09", reorganize, "baba\n"))

        frequency_string = case_generators.Case("aabbcc\n", "aabbcc\n", 6, "tie")
        self.assertTrue(judge.output_matches("b01", frequency_string, "ccbbaa\n"))

    def test_semantic_validators_reject_invalid_answers(self) -> None:
        pairs = case_generators.Case("2 2 2\n1 2\n1 2\n", "1 1\n1 2\n", 4, "tie")
        self.assertFalse(judge.output_matches("h02", pairs, "2 2\n2 2\n"))

        reorganize = case_generators.Case("aabb\n", "abab\n", 4, "tie")
        self.assertFalse(judge.output_matches("h09", reorganize, "aabb\n"))
        self.assertFalse(judge.output_matches("h09", reorganize, "IMPOSSIBLE\n"))

        frequency_string = case_generators.Case("aaabbc\n", "aaabbc\n", 6, "tie")
        self.assertFalse(judge.output_matches("b01", frequency_string, "bbaaac\n"))

    def test_exercise_files_compile_and_use_standard_entry_points(self) -> None:
        for _, filename in case_generators.EXERCISES.values():
            path = TOPIC / filename
            source = path.read_text(encoding="utf-8")
            compile(source, str(path), "exec")
            self.assertIn('if __name__ == "__main__":', source)


if __name__ == "__main__":
    unittest.main()
