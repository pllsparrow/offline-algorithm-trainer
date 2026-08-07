# Offline Algorithm Trainer

[中文说明](README.zh-CN.md)

I built this because I wanted a simple way to practise algorithms without
keeping a browser, an editor, and an online judge open at the same time.

The repository contains 150 interview problems grouped by topic. Each problem
has a Python starter file and local test cases, so the usual loop stays on your
machine:

```text
pick a problem -> write solution.py -> run it -> inspect the failing case
```

It also keeps a small SQLite progress file locally. Your attempts and completed
solutions are ignored by Git and are not part of this public repository.

## Getting started

Python 3.12 or newer is required. There are no third-party Python dependencies.

```bash
git clone https://github.com/pllsparrow/offline-algorithm-trainer.git
cd offline-algorithm-trainer

python train.py list
python train.py show two-sum
python train.py run two-sum
python train.py status
```

Open the `solution.py` path printed by `show`, write your solution, and run the
same problem again. A failed case prints its input, expected result, and actual
result.

For a stubborn failure, rerun only that case and keep your debug output:

```bash
python train.py run two-sum --case 1 --debug
```

You can also filter the list:

```bash
python train.py list --category graph
python train.py list --difficulty Hard
```

## ACM stdin/stdout mode

Function mode is useful for learning a pattern. ACM mode runs your file as a
standalone Python process, feeds it stdin, and compares stdout like an online
assessment:

```bash
python train.py scaffold --acm
python train.py run two-sum --mode acm
python train.py run two-sum --mode acm --all
```

ACM starters are named `solution_acm.py` and live beside the normal
`solution.py`. All 150 problems have an ACM entry and run in an independent
Python process. There are two input protocols:

- `text`: curated whitespace/line formats for the first high-value assessment
  problems, including arrays, sliding windows, trees, heaps, and basic DP.
- `json`: a uniform stdin/stdout format for the remaining signatures, including
  linked lists, trees, graphs, and stateful design problems. The adapter converts
  JSON into the same data structures used by function mode.

Inspect a problem's exact protocol before solving it:

```bash
python train.py show two-sum --mode acm
python train.py check --acm
```

`scripts/build_acm.py` deterministically regenerates all 150 specs from the
function-mode dataset while preserving the curated text formats in
`data/acm_text_specs.json`.

## Commands I use most

| Command | What it does |
| --- | --- |
| `python train.py list` | Lists problems and local progress |
| `python train.py show <slug>` | Shows the problem details and file path |
| `python train.py run <slug>` | Runs the local test cases |
| `python train.py run <slug> --case 1` | Repeats one failing case |
| `python train.py run <slug> --all` | Runs the remaining cases after a failure |
| `python train.py status` | Shows attempted and accepted totals |
| `python train.py check` | Checks the repository data |

The problems are arranged under `problems/` in 18 chapters, from arrays and
linked lists to graphs and dynamic programming. The judge is in `judge/`, while
problem metadata, tests, and your local progress live under `data/`.

## About the problem content

Problem names and links refer to exercises on LeetCode and NeetCode. This
repository contains my own summaries, hints, starter templates, test harness,
and local test data. It does not republish full commercial problem statements
or official solutions. See [NOTICE.md](NOTICE.md) for details.

The original code in this repository is released under the [MIT License](LICENSE).
