# Offline Algorithm Trainer

[简体中文](README.zh-CN.md)

A Python-first, fully offline algorithm practice environment with 150 curated
interview problems, local test cases, a lightweight judge, debugging support,
and persistent progress tracking.

## Why This Project

Most coding-practice workflows require switching between a browser, an editor,
and a remote judge. This project keeps the tight feedback loop local:

```text
choose a problem -> edit solution.py -> run tests -> inspect failure -> debug
```

It is designed for interview preparation, deliberate practice, and learning how
to debug algorithms rather than only submitting answers.

## Features

- 150 interview-focused problems across 18 chapters.
- Python solution templates organized by topic.
- Fully offline JSON test cases.
- Linked-list, tree, graph, and random-pointer structure conversion.
- Run one case, stop on first failure, or continue through all failures.
- Optional debug mode that preserves solution `print()` output.
- Local SQLite progress database with attempts and accepted status.
- Filters by category and difficulty.
- No account, cloud service, or third-party Python package required.

## Requirements

- Python 3.12+

## Quick Start

```bash
git clone https://github.com/pllsparrow/offline-algorithm-trainer.git
cd offline-algorithm-trainer

python train.py list
python train.py show two-sum
python train.py run two-sum
python train.py status
```

The first command creates `data/progress.sqlite3` locally. The file is ignored
by Git, so personal progress is never published.

## Daily Commands

| Command | Purpose |
| --- | --- |
| `python train.py list` | List problems, status, attempts, and categories |
| `python train.py show two-sum` | Show metadata, hints, signature, and file path |
| `python train.py run two-sum` | Run all local cases for one problem |
| `python train.py run two-sum --case 1` | Reproduce one case |
| `python train.py run two-sum --case 1 --debug` | Keep debug output for one case |
| `python train.py run two-sum --all` | Continue after failures |
| `python train.py status` | Show accepted and attempted totals |
| `python train.py check` | Validate repository metadata and test data |

Filters:

```bash
python train.py list --category graph
python train.py list --difficulty Hard
```

## Practice Workflow

Each problem has a workspace such as:

```text
problems/
  01-arrays-hashing/
    003-two-sum/
      README.md
      solution.py
```

1. Open the problem's `solution.py`.
2. State a brute-force approach and expected complexity.
3. Implement the solution.
4. Run `python train.py run <slug>`.
5. Compare `args`, `expected`, and `actual` on failure.
6. Re-run one failing case with `--debug` or an IDE breakpoint.
7. Explain the final time complexity, space complexity, and edge cases.

## Project Structure

- `train.py`: command-line entry point and progress management.
- `judge/python_judge.py`: isolated local Python judge.
- `support.py`: local linked-list, tree, graph, and node types.
- `problems/`: generated chapter and problem workspaces.
- `data/problems.json`: problem metadata and starter templates.
- `data/tests.json`: offline test cases.
- `data/progress.sqlite3`: local-only progress, created at runtime.
- `scripts/build_roadmap.py`: validates and rebuilds workspaces.

## Tests and Validation

```bash
python train.py check
python train.py run contains-duplicate
```

The repository intentionally does not publish a user's completed solutions or
progress database.

## Content Notice

Problem names and links refer to exercises hosted by LeetCode and NeetCode.
This repository provides original summaries, hints, templates, test harnesses,
and local test data; it does not redistribute copied commercial problem
statements or official platform solutions. See [NOTICE.md](NOTICE.md).

## Roadmap

- Add regression tests for the command-line application and judge.
- Improve failure diffs for nested structures.
- Add import/export for personal progress.
- Keep the core workflow offline and dependency-free.

## License

MIT for the original software in this repository. See [LICENSE](LICENSE) and
[NOTICE.md](NOTICE.md).
