#!/usr/bin/env python3
"""Interactive child-process runner for local white-box debugging."""

from __future__ import annotations

import base64
import io
import json
import sys
import traceback


SOURCE = base64.b64decode(sys.argv[1]).decode("utf-8")
INPUT_TEXT = base64.b64decode(sys.argv[2]).decode("utf-8")
BREAKPOINTS = {int(value) for value in sys.argv[3].split(",") if value}
CONTROL_INPUT = sys.stdin
CONTROL_OUTPUT = sys.stdout
MODE = "continue"
STEP_DEPTH = 0
MAX_VALUE_LENGTH = 240
MAX_OUTPUT_LENGTH = 65_536


class LimitedStringIO(io.StringIO):
    def write(self, text: str) -> int:
        remaining = MAX_OUTPUT_LENGTH - self.tell()
        if remaining > 0:
            super().write(text[:remaining])
        return len(text)


CAPTURED_OUTPUT = LimitedStringIO()


def compact(value: object) -> str:
    try:
        rendered = repr(value)
    except Exception:
        rendered = "<unavailable>"
    if len(rendered) <= MAX_VALUE_LENGTH:
        return rendered
    return rendered[: MAX_VALUE_LENGTH - 3] + "..."


def stack_for(frame) -> list[dict[str, object]]:
    stack = []
    current = frame
    while current is not None:
        if current.f_code.co_filename == "<solution>":
            stack.append({"function": current.f_code.co_name, "line": current.f_lineno})
        current = current.f_back
    stack.reverse()
    return stack


def send(payload: dict[str, object]) -> None:
    CONTROL_OUTPUT.write(json.dumps(payload, ensure_ascii=False) + "\n")
    CONTROL_OUTPUT.flush()


def pause(frame) -> None:
    global BREAKPOINTS, MODE, STEP_DEPTH
    send(
        {
            "state": "paused",
            "line": frame.f_lineno,
            "locals": {key: compact(value) for key, value in frame.f_locals.items()},
            "stack": stack_for(frame),
            "stdout": CAPTURED_OUTPUT.getvalue()[-65536:],
        }
    )
    command_line = CONTROL_INPUT.readline()
    if not command_line:
        raise SystemExit(0)
    command = json.loads(command_line)
    BREAKPOINTS = {int(value) for value in command.get("breakpoints", BREAKPOINTS)}
    MODE = command.get("command", "continue")
    STEP_DEPTH = len(stack_for(frame))
    if MODE == "stop":
        raise SystemExit(0)


def trace(frame, event, arg):
    if frame.f_code.co_filename != "<solution>" or event != "line":
        return trace
    depth = len(stack_for(frame))
    should_step = MODE == "step" and depth <= STEP_DEPTH
    if frame.f_lineno in BREAKPOINTS or should_step:
        pause(frame)
    return trace


def main() -> None:
    sys.stdin = io.StringIO(INPUT_TEXT)
    sys.stdout = CAPTURED_OUTPUT
    try:
        namespace = {"__name__": "__main__"}
        sys.settrace(trace)
        exec(compile(SOURCE, "<solution>", "exec"), namespace, namespace)
        sys.settrace(None)
        send({"state": "finished", "stdout": CAPTURED_OUTPUT.getvalue()[-65536:]})
    except SystemExit:
        raise
    except BaseException as error:
        sys.settrace(None)
        frames = traceback.extract_tb(error.__traceback__)
        solution_frames = [frame for frame in frames if frame.filename == "<solution>"]
        line = solution_frames[-1].lineno if solution_frames else None
        send(
            {
                "state": "error",
                "stdout": CAPTURED_OUTPUT.getvalue()[-65536:],
                "error": {
                    "type": type(error).__name__,
                    "message": str(error),
                    "line": line,
                    "traceback": "".join(traceback.format_exception(error))[-65536:],
                },
            }
        )


if __name__ == "__main__":
    main()
