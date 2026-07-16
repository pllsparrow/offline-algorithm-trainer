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

## Local Examples

### Case 1

```python
args = [['A', 'A', 'A', 'B', 'B', 'B'], 2]
expected = 8
```

### Case 2

```python
args = [['A', 'C', 'A', 'B', 'D', 'B'], 1]
expected = 6
```

### Case 3

```python
args = [['A', 'A', 'A', 'B', 'B', 'B'], 3]
expected = 10
```

### Case 4

```python
args = [['A'], 0]
expected = 1
```

### Case 5

```python
args = [['A', 'A'], 1]
expected = 3
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run task-scheduler
```
