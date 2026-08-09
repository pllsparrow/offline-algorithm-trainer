# Algorithm Training Protocol: Learn, Then Submit

This protocol is for the Mac. It treats algorithm practice as new knowledge
acquisition, not as review. The goal is to turn a problem pattern into code
that can be written under a time limit and in an ACM stdin/stdout environment.

## Two Modes, One Learning Loop

LeetCode-style practice and ACM-style practice are not competing systems.

| Mode | What it trains | How to use it |
| --- | --- | --- |
| Function mode | Pattern recognition, data structure, return value | Learn the idea and get a local test to pass |
| ACM mode | Input parsing, output formatting, complete program structure, time pressure | Submit the same idea as a standalone `solution.py` |

For a new topic, start in function mode. Once the idea is understood, rewrite
the same problem in ACM mode. Do not abandon LeetCode: it is the shortest path
to learning the pattern. ACM is the transfer step required by many online
assessments.

Each `solution.py` in this trainer starts completely empty. The learner must
write the imports, input parsing, algorithm, output, and program entry point.

## Beginner Session (90-120 Minutes)

1. **Concept, 10 minutes**: state what the data structure stores and what the
   loop invariant means. Draw one small example by hand.
2. **Template, 15 minutes**: type the smallest reusable template yourself.
   Do not paste a complete solution.
3. **Guided problem, 20 minutes**: solve one easy problem with hints. The
   stopping question is: what information must be remembered at each index?
4. **Independent problem, 25 minutes**: close the explanation and solve a
   nearby problem. If stuck, use the hint ladder below.
5. **ACM transfer, 15-25 minutes**: open the problem with
   `python3 train.py show <slug>`, write its `solution.py`, and run it with
   `python3 train.py run <slug>`.
6. **Explain, 5 minutes**: say the input, invariant, output, complexity, and
   one failure case aloud.

One new pattern per session is enough. A beginner who can independently solve
one problem and reproduce it the next day is progressing faster than someone
who reads ten solutions.

## Hint Ladder

Use only the next level when the current level is insufficient:

1. What is the input and what must be true after each loop iteration?
2. Which values must be remembered: a set, map, stack, queue, or two bounds?
3. Write pseudocode with no Python syntax.
4. Fill in one missing line or one state transition.
5. Read a complete solution only after recording the failed idea, then close it
   and reimplement from memory.

The tutor must ask before revealing the next level. After a solution passes,
the tutor asks: “Why does this line preserve the invariant?” and “What breaks
if the input is empty, duplicated, or already sorted?”

## ACM Python Minimum

Start every ACM solution as a complete program. Common patterns:

```python
import sys

tokens = sys.stdin.buffer.read().split()
numbers = list(map(int, tokens))

# parse numbers, compute the answer
sys.stdout.write(str(answer) + "\n")
```

For line-oriented strings, use `sys.stdin.readline().strip()` instead. Always
decide explicitly:

- How many test cases are there?
- Does the first line contain `n`, `k`, or both?
- Are values space-separated or line-separated?
- Should output contain one answer per line?

The ACM version is accepted only when the program can be started from an empty
process and communicates solely through stdin and stdout. Debug output must be
removed before submission.

The local judge enforces that process boundary. It feeds each test case to the
solution's stdin, captures stdout, normalises whitespace, and compares it with
the expected output.

## Daily Mac Checklist

- [ ] Start a timer before opening the problem.
- [ ] Write the invariant in one sentence before coding.
- [ ] Attempt independently for 25 minutes.
- [ ] If a hint is used, record its level (`question`, `clue`, `pseudocode`,
  `partial`, or `solution`).
- [ ] Run the function-mode local judge when one is available.
- [ ] Complete the same idea in this trainer's ACM mode.
- [ ] Explain time and space complexity aloud.
- [ ] Schedule the problem for next-day and fourth-day recall.

## Progress Metrics

Track these instead of raw problem count:

- `independent_passes`: passed without a solution or pseudocode
- `hint_level`: highest hint needed
- `acm_passes`: standalone stdin/stdout program passed
- `next_day_recall`: passed again without notes
- `explanation_pass`: can explain invariant and complexity in two minutes

A problem is learned only when `independent_passes`, `acm_passes`, and
`next_day_recall` are all true. A local “accepted” result without these fields
is only an attempt.

The trainer currently persists attempts and accepted runs in
`data/progress.sqlite3`. The other learning metrics are a manual learning
contract until the trainer implements dedicated fields for them.

## Current Sprint

For the Pinduoduo service-side assessment, follow this order:

1. Arrays, hash maps, two pointers, and sliding-window transfer to ACM.
2. Stack, queue, and monotonic stack.
3. Binary-tree DFS and BFS.
4. Heap and priority queue.
5. Graph BFS/DFS.
6. Basic one-dimensional dynamic programming and greedy methods.

Keep the daily LLM and computer-basics block separate. Do not start a new
framework or a new project during this sprint.

## Mac Tutor Prompt

```text
You are my strict but constructive algorithm tutor. I am learning this topic
for the first time. Ask me to predict the invariant and input format before
showing code. Use the hint ladder: question -> clue -> pseudocode -> one-line
scaffold -> complete solution only when necessary. After the function-mode
solution passes, require an ACM stdin/stdout rewrite and ask me to explain
complexity and one edge case. Do not count reading a solution as mastery.
```
