# Algorithm Training Camp V1 Technical Specification

Status: Draft for implementation

## Services

The algorithm trainer is an independent local service. The expected development layout is:

```text
saveJob frontend/backend      existing ports and startup
algorithm trainer web         127.0.0.1:8765
algorithm trainer database    data/progress.sqlite3
```

V1 does not copy the trainer into a machine-specific saveJob path. saveJob adds a link to the trainer. The
trainer owns its题目 files, test data, drafts, submissions, and progress.

## Runtime and Safety

- Python interpreter: Python 3.12, selected by explicit configuration.
- The API binds to `127.0.0.1` by default.
- Every execution is a child process with a five-second timeout and bounded output.
- The child process receives only the submitted source and selected stdin.
- V1 local mode may write a submitted source to the selected `hot_150` path after testing.
- The child process must not be used as a public or network-facing code execution endpoint.

## Data Sources

- `data/problems.json`: title, slug, index, category, difficulty, links, starter metadata.
- `data/acm_tests.json`: deterministic judge cases and expected stdout.
- `data/examples.json` (new): 2-3 curated examples per slug. Each example contains `name`,
  `stdin`, `stdout`, and a short `reason` explaining why the case is representative.
- `hot_150/qNNN_*.py`: the editable submitted source of truth for V1.
- `data/progress.sqlite3`: drafts, submissions, and progress records.

## HTTP API

### `GET /api/problems`

Returns compact navigation records: `index`, `slug`, `title`, `difficulty`, `category`, and
progress status. The UI uses number jump and filters instead of rendering all 150 records at once.

### `GET /api/problems/{index}`

Returns problem metadata, source text, ACM format, NeetCode URL, curated examples, draft source,
and current progress. The path is validated against the metadata table and cannot escape the
repository root.

### `POST /api/drafts/{index}`

Stores the browser editor source in SQLite. Draft writes are idempotent and do not modify the
problem file.

### `POST /api/run`

Input: `index`, `source`, `stdin`, and optional `breakpoints`. Runs one custom payload and returns
stdout, stderr, structured error data, and a compact trace. This endpoint does not write files.

### `POST /api/submit`

Input: `index` and `source`. Stores a temporary submission, runs the problem's complete
deterministic case set (normally around 100 cases), writes the source to `hot_150/` after the run,
and records accepted/failed status. The response contains the first failing case plus aggregate
counts, not all output from all cases.

### `POST /api/debug/start`, `/api/debug/step`, `/api/debug/continue`, `/api/debug/stop`

These endpoints manage a short-lived local debug session. The session owns one child process,
its stdin payload, current frame, breakpoint set, and trace cursor. Sessions expire after five
minutes of inactivity and are never persisted.

## Debugger Semantics

The debugger uses Python tracing in a child process. V1 supports:

- Line breakpoints in the submitted file.
- Pause when a breakpoint line is reached.
- Continue to the next breakpoint or program exit.
- Step over one user-code line.
- Current line and source location.
- Locals for the current frame and a compact call stack.
- Captured stdout and the exception type, message, and traceback line.

V1 does not support stepping into libraries, changing variables, conditional breakpoints,
watch expressions, threads, or remote sessions. The UI shows only breakpoint snapshots, the
latest state, and error state by default. The complete trace is available only as an explicit
diagnostic expansion.

The main debugger remains line-oriented and PyCharm-style. A post-V1 Notebook surface may support
executable algorithm notes and small data experiments, but its kernel state must remain isolated
from ACM runs and submissions. Text-only written-test and interview notes remain Markdown files.

## Submit Semantics

Normal run uses the curated examples or one custom stdin payload. Submit uses every fixed case
materialized for that problem. The normal target is approximately 100 deterministic, unique
cases, but problems with a naturally small valid input domain may use fewer without padding the
dataset with duplicates. Generated cases are materialized into versioned data rather than
generated at request time. A submit writes the source after the full run, whether accepted or
failed, and records the result and timestamp.

## Persistence Schema

SQLite tables:

- `drafts(problem_index PRIMARY KEY, source, updated_at)`
- `submissions(id, problem_index, source, status, passed, total, first_failure_json, created_at)`
- `progress(problem_index PRIMARY KEY, status, attempts, accepted, updated_at)`

No production saveJob data is read or written by V1.

## Frontend Layout

- Left: compact problem number jump, search/filter, and virtualized/scrollable results.
- Center: code editor and Run/Reset controls.
- Right: problem ACM format, curated examples, stdin editor, breakpoint input, output, error, and
  compact variable snapshots.
- Text uses readable desktop sizing and responsive stacking on narrow screens.

## Verification

- Unit tests for metadata/example loading, ACM parsing, draft persistence, and submit aggregation.
- Integration tests for syntax errors, runtime errors, timeout, custom stdin, breakpoints, and
  successful/failed submissions.
- Browser smoke test: jump to 1, 60, and 150; edit code; run a sample; hit a breakpoint; inspect
  locals; submit a known-correct solution.
