# 134. Meeting Rooms II

- Chapter: 16. Intervals
- Difficulty: Medium
- Source: https://leetcode.com/problems/meeting-rooms-ii/
- Reference: https://neetcode.io/problems/meeting-schedule-ii?list=neetcode150

## Goal

Classic interview problem for Meeting Rooms II. Practice sorting then merging and overlap checks. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: sorting then merging.
- Before coding, state the invariant or state definition: overlap checks.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [[[0, 30], [5, 10], [15, 20]]]
expected = 2
```

### Case 2

```python
args = [[[7, 10], [2, 4]]]
expected = 1
```

### Case 3

```python
args = [[[1, 5]]]
expected = 1
```

### Case 4

```python
args = [[[1, 5], [8, 9]]]
expected = 1
```

### Case 5

```python
args = [[[1, 5], [2, 6]]]
expected = 2
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run meeting-rooms-ii
```
