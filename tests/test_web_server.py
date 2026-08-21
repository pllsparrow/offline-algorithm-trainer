import importlib.util
import unittest


WEB_DEPENDENCIES_INSTALLED = importlib.util.find_spec("fastapi") is not None and importlib.util.find_spec("httpx") is not None


@unittest.skipUnless(WEB_DEPENDENCIES_INSTALLED, "FastAPI web dependencies are not installed")
class FastApiServerTests(unittest.TestCase):
    def test_problem_and_static_editor_routes(self) -> None:
        from fastapi.testclient import TestClient
        from web_debug_server import app

        with TestClient(app) as client:
            problem = client.get("/api/problems/64")
            editor = client.get("/assets/editor.bundle.js")

        self.assertEqual(200, problem.status_code)
        self.assertEqual("Task Scheduler", problem.json()["title"])
        self.assertEqual(3, len(problem.json()["examples"]))
        self.assertEqual(200, editor.status_code)
        self.assertIn("createPythonEditor", editor.text)

    def test_request_validation_is_structured(self) -> None:
        from fastapi.testclient import TestClient
        from web_debug_server import app

        with TestClient(app) as client:
            response = client.post("/api/run", json={"index": 0, "source": "print(1)", "stdin": ""})

        self.assertEqual(422, response.status_code)
        self.assertEqual("greater_than_equal", response.json()["detail"][0]["type"])


if __name__ == "__main__":
    unittest.main()
