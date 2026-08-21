import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOPIC = ROOT / "muscle_memory" / "recursion"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


sys.path.insert(0, str(TOPIC))
case_generators = load_module("recursion_cases", TOPIC / "case_generators.py")
judge = load_module("recursion_judge", TOPIC / "judge.py")


class RecursionDrillTests(unittest.TestCase):
    def test_each_exercise_has_49_unique_cases(self) -> None:
        self.assertEqual(20, len(case_generators.EXERCISES))
        for exercise_id in case_generators.EXERCISES:
            cases = case_generators.build_cases(exercise_id)
            self.assertEqual(49, len(cases), exercise_id)
            self.assertEqual(49, len({case.stdin for case in cases}), exercise_id)

    def test_titles_do_not_duplicate_hot_150(self) -> None:
        import json

        hot_titles = {
            problem["title"].casefold()
            for problem in json.loads((ROOT / "data" / "problems.json").read_text(encoding="utf-8"))
        }
        drill_titles = {title.casefold() for title, _ in case_generators.EXERCISES.values()}
        self.assertFalse(hot_titles & drill_titles)

    def test_exercise_files_compile_and_have_entry_points(self) -> None:
        for _, filename in case_generators.EXERCISES.values():
            path = TOPIC / filename
            source = path.read_text(encoding="utf-8")
            compile(source, str(path), "exec")
            self.assertIn('if __name__ == "__main__":', source)


if __name__ == "__main__":
    unittest.main()
