# Offline Algorithm Trainer

[中文说明](README.zh-CN.md)

I built this because I wanted a simple way to practise algorithms without
keeping a browser, an editor, and an online judge open at the same time.

The repository contains 150 interview problems in the `hot_150/` directory.
Every question is an ACM-style program: its Python file reads from stdin, writes to
stdout, and the judge compares the output exactly (whitespace-normalised). This
mirrors a real online assessment environment, so the usual loop stays on your
machine:

```text
pick a problem -> write its question file -> run it -> inspect the failing case
```

It also keeps a small SQLite progress file locally. Your attempts and completed
solutions are ignored by Git and are not part of this public repository.

If you are learning a pattern for the first time rather than reviewing it,
start with the [learning protocol](docs/learning_protocol.md). It defines the
function-to-ACM transfer, hint ladder, daily session, and mastery criteria.
All NeetCode problem links are collected in the
[central problem index](docs/neetcode_links.md).

## Getting started

Python 3.12 or newer is required. There are no third-party Python dependencies.

```bash
git clone https://github.com/pllsparrow/offline-algorithm-trainer.git
cd offline-algorithm-trainer

python3 train.py list
python3 train.py show two-sum
python3 train.py run two-sum
python3 train.py run 003
python3 train.py status
```

## Browser training camp

Install the web dependencies once, then start the local-only service:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-web.txt
.venv/bin/python web_debug_server.py
```

Set `ALGORITHM_TRAINER_PYTHON` when the service should use a specific Python
3.12 interpreter for submitted programs.

The API uses FastAPI and exposes local documentation at `/api/docs`. The editor
is a locally bundled CodeMirror 6 build with Python highlighting, four-space
indentation, visible spaces, and breakpoint gutters. Run `npm install && npm run
build:web` only when changing `web/editor.js`.

Then open `http://127.0.0.1:8765`. The browser app provides problem navigation,
SQLite drafts, curated examples, custom runs, full submissions, breakpoints,
continue, step over, locals, and a compact call stack. A submission runs the
problem's complete fixed case set and writes the source back to `hot_150/` after
the run finishes.

Open the `qNNN_problem_name.py` path printed by `show`. The file contains only
short `Input` and `Output` comments, so write the input parsing, algorithm,
output, and program entry point yourself. Then run the same problem again. A
failed case prints its stdin, expected stdout, and actual stdout.

For a stubborn failure, rerun only that case:

```bash
python3 train.py run two-sum --case 1
```

You can also filter the list:

```bash
python3 train.py list --category graph
python3 train.py list --difficulty Hard
```

## ACM text protocol

All 150 problems use a pure text protocol. Each test case has a stdin payload
and an expected stdout payload. The judge runs your file as an independent
Python process, feeds it the stdin, captures stdout, and compares it
(whitespace-normalised) against the expected output.

Each of 148 problems has 50 distinct cases covering boundaries, duplicates,
extreme values, sizes, and structural shapes. `generate-parentheses` and
`n-queens` use 9 and 10 exhaustive/boundary inputs instead; their valid input
domains are too small to justify padding the corpus with duplicates.

Common input formats:

- **Integer list**: count `n` on one line, then `n` integers on the next.
- **Single integer / float / string token**: one line.
- **Whole line string** (may contain spaces): one line, read with `readline`.
- **Integer matrix**: `r c` on the first line, then `r` lines of `c` integers.
- **Character board**: `r c` on the first line, then `r` lines of `c` chars.
- **Binary tree**: count `n`, then `n` level-order values (`null` for missing).
- **Graph adjacency**: count `n`, then per node degree `d` and `d` neighbour ids.
- **Linked list**: count `n`, then `n` integers.
- **Operations (design problems)**: first line `q` (operation count), then `q`
  lines of `op args...`. Output one result per operation (`null` for void).

For problems with multiple valid answers (e.g. `group-anagrams`, `3sum`,
`subsets`), the expected output is canonicalised (sorted), so you must print in
the same sorted order to pass.

Inspect a problem's exact format before solving it:

```bash
python3 train.py show two-sum
python3 train.py check
```

`scripts/build_acm.py` deterministically regenerates all 150 specs from
`data/problems.json` and `data/tests.json`.

## Commands I use most

| Command | What it does |
| --- | --- |
| `python3 train.py list` | Lists problems and local progress |
| `python3 train.py show <slug>` | Shows the problem details, ACM format, and file path |
| `python3 train.py run <slug>` | Runs the local ACM test cases |
| `python3 train.py run <number>` | Runs by problem number, for example `run 001` |
| `python3 train.py run <slug> --case 1` | Repeats one failing case |
| `python3 train.py run <slug> --all` | Runs the remaining cases after a failure |
| `python3 train.py status` | Shows attempted and accepted totals |
| `python3 train.py check` | Checks the repository data |
| `python3 train.py scaffold --force` | Resets all question files to their I/O comments |

PyCharm users can select the shared `Judge Current Solution` run configuration once. After that, open any file in `hot_150/` and use the green Run button to judge the current file.

All 150 Python files are stored directly under `hot_150/` and named like
`q001_contains_duplicate.py`. The judge is in `judge/`, while problem metadata,
tests, and your local progress live under `data/`.

Heap and bucket follow-up exercises live in
[`muscle_memory/heapq&buckets/`](muscle_memory/heapq&buckets/README.md). This set
contains fifteen interview-focused variants with 99 deterministic cases each and
semantic validators for problems that allow tied answers.

Recursion drills live in
[`muscle_memory/recursion/`](muscle_memory/recursion/README.md). The twenty
exercises cover recursion fundamentals, search, divide and conquer, and tree
recursion. Ten are tree-focused, with 49 deterministic cases per exercise.

## About the problem content

Problem names and links refer to exercises on LeetCode and NeetCode. This
repository contains my own summaries, hints, starter templates, test harness,
and local test data. It does not republish full commercial problem statements
or official solutions. See [NOTICE.md](NOTICE.md) for details.

The original code in this repository is released under the [MIT License](LICENSE).
