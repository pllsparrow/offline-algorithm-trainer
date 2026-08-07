# 064. Task Scheduler

- Chapter: 08. Heap / Priority Queue
- Difficulty: Medium
- Source: https://leetcode.com/problems/task-scheduler/
- Reference: https://neetcode.io/problems/task-scheduling?list=neetcode150

## Goal

Classic interview problem for Task Scheduler. Practice Top K and two heaps. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: Top K.
- Before coding, state the invariant or state definition: two heaps.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: arg1: a string list: count n then n tokens; arg2: an integer. Output: the integer.

## Local Examples

### Case 1

**Input**

```
6
A
A
A
B
B
B
2
```

**Output**

```
8
```

### Case 2

**Input**

```
6
A
C
A
B
D
B
1
```

**Output**

```
6
```

### Case 3

**Input**

```
6
A
A
A
B
B
B
3
```

**Output**

```
10
```

## Run

```bash
python3 train.py run task-scheduler
```
