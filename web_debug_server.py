#!/usr/bin/env python3
"""FastAPI entry point for the local Algorithm Training Camp."""

from __future__ import annotations

import sys
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from web_app import ApiError, AppService, MAX_INPUT_BYTES, MAX_SOURCE_BYTES, validate_text


ROOT = Path(__file__).resolve().parent
SERVICE = AppService(ROOT)
app = FastAPI(title="Algorithm Training Camp", docs_url="/api/docs", redoc_url=None)
app.mount("/assets", StaticFiles(directory=ROOT / "web" / "assets"), name="assets")


class DraftPayload(BaseModel):
    source: str


class RunPayload(BaseModel):
    index: int = Field(ge=1, le=150)
    source: str
    stdin: str = ""


class SubmitPayload(BaseModel):
    index: int = Field(ge=1, le=150)
    source: str


class DebugStartPayload(RunPayload):
    breakpoints: list[int] = Field(default_factory=list)


class DebugCommandPayload(BaseModel):
    session_id: str
    breakpoints: list[int] = Field(default_factory=list)


class DebugStopPayload(BaseModel):
    session_id: str


@app.exception_handler(ApiError)
async def api_error_handler(_request: Request, error: ApiError) -> JSONResponse:
    return JSONResponse(status_code=error.status, content={"error": error.message})


@app.get("/", include_in_schema=False)
async def index() -> FileResponse:
    return FileResponse(ROOT / "web" / "index.html")


@app.get("/api/problems")
async def list_problems() -> list[dict]:
    return SERVICE.list_problems()


@app.get("/api/problems/{index}")
async def get_problem(index: int) -> dict:
    return SERVICE.get_problem(index)


@app.post("/api/drafts/{index}")
async def save_draft(index: int, payload: DraftPayload) -> dict:
    return SERVICE.save_draft(index, payload.source)


@app.post("/api/run")
async def run(payload: RunPayload) -> dict:
    return SERVICE.run(payload.model_dump())


@app.post("/api/submit")
async def submit(payload: SubmitPayload) -> dict:
    return SERVICE.submit(payload.model_dump())


@app.post("/api/debug/start")
async def debug_start(payload: DebugStartPayload) -> dict:
    SERVICE.repository.problem(payload.index)
    source = validate_text(payload.source, "source", MAX_SOURCE_BYTES)
    stdin = validate_text(payload.stdin, "stdin", MAX_INPUT_BYTES)
    session_id, event = SERVICE.debugger.start(source, stdin, payload.breakpoints)
    return {"session_id": session_id, **event}


@app.post("/api/debug/step")
async def debug_step(payload: DebugCommandPayload) -> dict:
    return SERVICE.debugger.command(payload.session_id, "step", payload.breakpoints)


@app.post("/api/debug/continue")
async def debug_continue(payload: DebugCommandPayload) -> dict:
    return SERVICE.debugger.command(payload.session_id, "continue", payload.breakpoints)


@app.post("/api/debug/stop")
async def debug_stop(payload: DebugStopPayload) -> dict:
    SERVICE.debugger.stop(payload.session_id)
    return {"state": "stopped"}


def main() -> None:
    try:
        import uvicorn
    except ImportError as error:
        raise SystemExit("Install web dependencies first: python3 -m pip install -r requirements-web.txt") from error
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
    uvicorn.run(app, host="127.0.0.1", port=port, reload=False)


if __name__ == "__main__":
    main()
