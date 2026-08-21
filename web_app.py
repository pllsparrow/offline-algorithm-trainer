#!/usr/bin/env python3
"""Application services for the local Algorithm Training Camp."""

from __future__ import annotations

import base64
import json
import os
import selectors
import sqlite3
import subprocess
import sys
import tempfile
import threading
import time
import uuid
from collections import Counter
from contextlib import contextmanager
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

MAX_SOURCE_BYTES = 256_000
MAX_INPUT_BYTES = 256_000
MAX_OUTPUT_BYTES = 65_536
RUN_TIMEOUT_SECONDS = 5
DEBUG_SESSION_TTL_SECONDS = 300
PYTHON_EXECUTABLE = os.environ.get("ALGORITHM_TRAINER_PYTHON", sys.executable)


class ApiError(Exception):
    def __init__(self, status: int, message: str) -> None:
        super().__init__(message)
        self.status = status
        self.message = message


def comparable_text(text: str) -> str:
    return " ".join(text.split())


def valid_top_k_frequent(stdin: str, actual: str) -> bool:
    try:
        tokens = list(map(int, stdin.split()))
        count = tokens[0]
        values = tokens[1 : count + 1]
        requested = tokens[count + 1]
        answer = list(map(int, actual.split()))
    except (IndexError, ValueError):
        return False
    frequencies = Counter(values)
    if not 1 <= requested <= len(frequencies):
        return False
    if len(answer) != requested or len(set(answer)) != requested or answer != sorted(answer):
        return False
    cutoff = sorted(frequencies.values(), reverse=True)[requested - 1]
    required = {value for value, frequency in frequencies.items() if frequency > cutoff}
    allowed = {value for value, frequency in frequencies.items() if frequency >= cutoff}
    return required <= set(answer) <= allowed


def output_matches(validator: str | None, stdin: str, actual: str, expected: str) -> bool:
    if validator == "top_k_frequent":
        return valid_top_k_frequent(stdin, actual)
    return comparable_text(actual) == comparable_text(expected)


def now_text() -> str:
    return datetime.now().isoformat(timespec="seconds")


def diagnostic_hint(error_type: str | None, message: str) -> str | None:
    if error_type == "SyntaxError":
        return "Check brackets, colons, and indentation near the reported line."
    if error_type == "IndexError":
        return "Confirm that the index is smaller than the list length before access."
    if error_type == "NameError":
        return "Check the spelling and scope of the variable or function name."
    if error_type == "ValueError" and "unpack" in message:
        return "Check that split() returns the same number of values as the assignment expects."
    if error_type == "RecursionError":
        return "Check the base case and confirm that every call reduces the problem."
    return None


class Repository:
    def __init__(self, root: Path) -> None:
        self.root = root.resolve()
        self.data = self.root / "data"
        self.problems = json.loads((self.data / "problems.json").read_text(encoding="utf-8"))
        self.specs = json.loads((self.data / "acm_tests.json").read_text(encoding="utf-8"))
        examples_path = self.data / "examples.json"
        self.examples = json.loads(examples_path.read_text(encoding="utf-8")) if examples_path.exists() else {}
        self.by_index = {problem["index"]: problem for problem in self.problems}

    def problem(self, index: int) -> dict[str, Any]:
        problem = self.by_index.get(index)
        if problem is None:
            raise ApiError(404, "Problem not found")
        return problem

    def solution_path(self, problem: dict[str, Any]) -> Path:
        path = (self.root / problem["path"]).resolve()
        questions = (self.root / "hot_150").resolve()
        if questions not in path.parents or path.suffix != ".py":
            raise ApiError(400, "Invalid solution path")
        return path

    def save_solution(self, problem: dict[str, Any], source: str) -> Path:
        path = self.solution_path(problem)
        descriptor, temporary_name = tempfile.mkstemp(dir=path.parent, prefix=f".{path.name}.", suffix=".tmp")
        temporary_path = Path(temporary_name)
        try:
            with os.fdopen(descriptor, "w", encoding="utf-8") as file:
                file.write(source)
                file.flush()
                os.fsync(file.fileno())
            os.replace(temporary_path, path)
        finally:
            temporary_path.unlink(missing_ok=True)
        return path


class Store:
    def __init__(self, path: Path) -> None:
        self.path = path
        self._lock = threading.Lock()
        self.initialize()

    @contextmanager
    def connect(self):
        connection = sqlite3.connect(self.path)
        connection.row_factory = sqlite3.Row
        try:
            yield connection
            connection.commit()
        finally:
            connection.close()

    def initialize(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.connect() as connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS drafts (
                    problem_index INTEGER PRIMARY KEY,
                    source TEXT NOT NULL,
                    updated_at TEXT NOT NULL
                )
                """
            )
            connection.execute(
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
            connection.execute(
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
            columns = {row["name"] for row in connection.execute("PRAGMA table_info(submissions)")}
            additions = {
                "problem_index": "INTEGER",
                "passed": "INTEGER",
                "total": "INTEGER",
                "first_failure_json": "TEXT",
            }
            for name, kind in additions.items():
                if name not in columns:
                    connection.execute(f"ALTER TABLE submissions ADD COLUMN {name} {kind}")
            connection.execute("CREATE INDEX IF NOT EXISTS idx_submissions_problem_created ON submissions(problem_index, created_at)")
            connection.execute("PRAGMA optimize")

    def progress(self) -> dict[str, dict[str, Any]]:
        with self.connect() as connection:
            rows = connection.execute("SELECT * FROM progress").fetchall()
        return {row["slug"]: dict(row) for row in rows}

    def draft(self, index: int) -> dict[str, Any] | None:
        with self.connect() as connection:
            row = connection.execute("SELECT source, updated_at FROM drafts WHERE problem_index = ?", (index,)).fetchone()
        return dict(row) if row else None

    def save_draft(self, index: int, source: str) -> str:
        updated_at = now_text()
        with self._lock, self.connect() as connection:
            connection.execute(
                """
                INSERT INTO drafts(problem_index, source, updated_at) VALUES (?, ?, ?)
                ON CONFLICT(problem_index) DO UPDATE SET source=excluded.source, updated_at=excluded.updated_at
                """,
                (index, source, updated_at),
            )
        return updated_at

    def record_submission(self, problem: dict[str, Any], source: str, result: dict[str, Any]) -> None:
        status = "accepted" if result["ok"] else "failed"
        timestamp = now_text()
        first_failure = result.get("first_failure")
        with self._lock, self.connect() as connection:
            connection.execute(
                """
                INSERT INTO submissions(
                    slug, status, code, result_json, created_at,
                    problem_index, passed, total, first_failure_json
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    problem["slug"], status, source, json.dumps(result, ensure_ascii=False), timestamp,
                    problem["index"], result["passed"], result["total"],
                    json.dumps(first_failure, ensure_ascii=False) if first_failure else None,
                ),
            )
            connection.execute(
                """
                INSERT INTO progress(slug, status, attempts, accepted, updated_at)
                VALUES (?, ?, 1, ?, ?)
                ON CONFLICT(slug) DO UPDATE SET
                    status=excluded.status,
                    attempts=progress.attempts + 1,
                    accepted=progress.accepted + excluded.accepted,
                    updated_at=excluded.updated_at
                """,
                (problem["slug"], status, int(result["ok"]), timestamp),
            )


def validate_text(value: Any, field: str, limit: int) -> str:
    if not isinstance(value, str):
        raise ApiError(400, f"{field} must be a string")
    if len(value.encode("utf-8")) > limit:
        raise ApiError(413, f"{field} is too large")
    return value


def parse_runtime_error(stderr: str) -> dict[str, Any] | None:
    if not stderr:
        return None
    lines = stderr.rstrip().splitlines()
    last = lines[-1] if lines else "Runtime error"
    error_type, separator, message = last.partition(":")
    line = None
    for item in reversed(lines):
        if 'File "<solution>", line ' in item:
            try:
                line = int(item.split('line ', 1)[1].split(',', 1)[0])
            except ValueError:
                pass
            break
    return {
        "type": error_type if separator else "RuntimeError",
        "message": message.strip() if separator else last,
        "line": line,
        "traceback": stderr[-MAX_OUTPUT_BYTES:],
        "hint": diagnostic_hint(error_type if separator else None, message),
    }


def execute(source: str, stdin: str, timeout: int = RUN_TIMEOUT_SECONDS, python_executable: str = PYTHON_EXECUTABLE) -> dict[str, Any]:
    with tempfile.TemporaryFile(mode="w+t", encoding="utf-8") as stdout_file, tempfile.TemporaryFile(mode="w+t", encoding="utf-8") as stderr_file:
        try:
            process = subprocess.run(
                [python_executable, "-c", compile_wrapper(source)],
                input=stdin,
                text=True,
                stdout=stdout_file,
                stderr=stderr_file,
                timeout=timeout,
                env={**os.environ, "PYTHONUNBUFFERED": "1"},
            )
        except subprocess.TimeoutExpired:
            stdout_file.seek(0)
            return {"ok": False, "stdout": stdout_file.read(MAX_OUTPUT_BYTES), "stderr": "", "timed_out": True, "error": {"type": "TimeoutError", "message": f"Execution exceeded {timeout} seconds", "line": None, "hint": "Check that every loop or recursive call makes progress toward termination."}}
        stdout_file.seek(0)
        stderr_file.seek(0)
        stdout = stdout_file.read(MAX_OUTPUT_BYTES)
        stderr = stderr_file.read(MAX_OUTPUT_BYTES)
    return {
        "ok": process.returncode == 0,
        "stdout": stdout,
        "stderr": stderr,
        "returncode": process.returncode,
        "timed_out": False,
        "error": parse_runtime_error(stderr) if process.returncode else None,
    }


def compile_wrapper(source: str) -> str:
    encoded = base64.b64encode(source.encode("utf-8")).decode("ascii")
    return f"import base64, resource\nresource.setrlimit(resource.RLIMIT_FSIZE, ({MAX_OUTPUT_BYTES}, {MAX_OUTPUT_BYTES}))\nexec(compile(base64.b64decode({encoded!r}), '<solution>', 'exec'), {{'__name__': '__main__'}})"


@dataclass
class DebugSession:
    process: subprocess.Popen[str]
    touched_at: float


class DebugManager:
    def __init__(self, runner: Path, python_executable: str = PYTHON_EXECUTABLE) -> None:
        self.runner = runner
        self.python_executable = python_executable
        self.sessions: dict[str, DebugSession] = {}
        self.lock = threading.Lock()

    def _read_event(self, process: subprocess.Popen[str], timeout: int = RUN_TIMEOUT_SECONDS) -> dict[str, Any]:
        selector = selectors.DefaultSelector()
        assert process.stdout is not None
        selector.register(process.stdout, selectors.EVENT_READ)
        if not selector.select(timeout):
            process.kill()
            raise ApiError(408, "Debug session timed out")
        line = process.stdout.readline()
        if not line:
            stderr = process.stderr.read() if process.stderr else ""
            raise ApiError(500, stderr or "Debug process exited unexpectedly")
        return json.loads(line)

    def start(self, source: str, stdin: str, breakpoints: list[int]) -> tuple[str, dict[str, Any]]:
        self.expire()
        session_id = uuid.uuid4().hex
        process = subprocess.Popen(
            [
                self.python_executable,
                str(self.runner),
                base64.b64encode(source.encode()).decode(),
                base64.b64encode(stdin.encode()).decode(),
                ",".join(map(str, breakpoints)),
            ],
            text=True,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            bufsize=1,
        )
        event = self._read_event(process)
        if event["state"] == "paused":
            with self.lock:
                self.sessions[session_id] = DebugSession(process, time.monotonic())
        else:
            process.wait(timeout=1)
        return session_id, event

    def command(self, session_id: str, command: str, breakpoints: list[int] | None = None) -> dict[str, Any]:
        self.expire()
        with self.lock:
            session = self.sessions.get(session_id)
        if session is None:
            raise ApiError(404, "Debug session not found or expired")
        assert session.process.stdin is not None
        session.process.stdin.write(json.dumps({"command": command, "breakpoints": breakpoints or []}) + "\n")
        session.process.stdin.flush()
        event = self._read_event(session.process)
        session.touched_at = time.monotonic()
        if event["state"] != "paused":
            self.stop(session_id, terminate=False)
        return event

    def stop(self, session_id: str, terminate: bool = True) -> None:
        with self.lock:
            session = self.sessions.pop(session_id, None)
        if not session:
            return
        if terminate and session.process.poll() is None:
            session.process.terminate()
        try:
            session.process.wait(timeout=1)
        except subprocess.TimeoutExpired:
            session.process.kill()
            session.process.wait(timeout=1)
        for stream in (session.process.stdin, session.process.stdout, session.process.stderr):
            if stream:
                stream.close()

    def expire(self) -> None:
        cutoff = time.monotonic() - DEBUG_SESSION_TTL_SECONDS
        with self.lock:
            expired = [key for key, value in self.sessions.items() if value.touched_at < cutoff]
        for session_id in expired:
            self.stop(session_id)


class AppService:
    def __init__(self, root: Path, db_path: Path | None = None, python_executable: str = PYTHON_EXECUTABLE) -> None:
        self.repository = Repository(root)
        self.store = Store(db_path or self.repository.data / "progress.sqlite3")
        self.python_executable = python_executable
        self.debugger = DebugManager(self.repository.root / "web_debug_runner.py", python_executable)

    def list_problems(self) -> list[dict[str, Any]]:
        progress = self.store.progress()
        return [
            {
                key: problem[key]
                for key in ("index", "slug", "title", "difficulty", "category")
            }
            | {"progress": progress.get(problem["slug"], {}).get("status", "todo")}
            for problem in self.repository.problems
        ]

    def get_problem(self, index: int) -> dict[str, Any]:
        problem = self.repository.problem(index)
        source = self.repository.solution_path(problem).read_text(encoding="utf-8")
        draft = self.store.draft(index)
        spec = self.repository.specs[problem["slug"]]
        return {
            **problem,
            "source": source,
            "draft_source": draft["source"] if draft else None,
            "draft_updated_at": draft["updated_at"] if draft else None,
            "format": spec["format"],
            "examples": self.repository.examples.get(problem["slug"], []),
            "progress": self.store.progress().get(problem["slug"], {"status": "todo", "attempts": 0, "accepted": 0}),
        }

    def save_draft(self, index: int, source: Any) -> dict[str, Any]:
        self.repository.problem(index)
        checked = validate_text(source, "source", MAX_SOURCE_BYTES)
        return {"ok": True, "updated_at": self.store.save_draft(index, checked)}

    def run(self, payload: dict[str, Any]) -> dict[str, Any]:
        self.repository.problem(int(payload.get("index", 0)))
        source = validate_text(payload.get("source"), "source", MAX_SOURCE_BYTES)
        stdin = validate_text(payload.get("stdin", ""), "stdin", MAX_INPUT_BYTES)
        return execute(source, stdin, python_executable=self.python_executable)

    def submit(self, payload: dict[str, Any]) -> dict[str, Any]:
        problem = self.repository.problem(int(payload.get("index", 0)))
        source = validate_text(payload.get("source"), "source", MAX_SOURCE_BYTES)
        saved_path = self.repository.save_solution(problem, source)
        self.store.save_draft(problem["index"], source)
        spec = self.repository.specs[problem["slug"]]
        passed = 0
        first_failure = None
        for case_number, case in enumerate(spec["cases"], start=1):
            execution = execute(source, case["stdin"], python_executable=self.python_executable)
            accepted = execution["ok"] and output_matches(spec.get("validator"), case["stdin"], execution["stdout"], case["stdout"])
            if accepted:
                passed += 1
            elif first_failure is None:
                first_failure = {
                    "case": case_number,
                    "stdin": case["stdin"],
                    "expected": case["stdout"],
                    "actual": execution["stdout"],
                    "error": execution.get("error"),
                }
        result = {
            "ok": first_failure is None,
            "passed": passed,
            "total": len(spec["cases"]),
            "first_failure": first_failure,
            "saved": True,
            "saved_path": str(saved_path.relative_to(self.repository.root)),
        }
        self.store.record_submission(problem, source, result)
        return result
