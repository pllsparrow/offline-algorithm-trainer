# 132. Non Overlapping Intervals

- Chapter: 16. Intervals
- Difficulty: Medium
- Source: https://leetcode.com/problems/non-overlapping-intervals/
- Reference: https://neetcode.io/problems/non-overlapping-intervals?list=neetcode150

## Goal

Classic interview problem for Non Overlapping Intervals. Practice sorting then merging and overlap checks. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: sorting then merging.
- Before coding, state the invariant or state definition: overlap checks.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [[[1, 2], [2, 3], [3, 4], [1, 3]]]
expected = 1
```

### Case 2

```python
args = [[[1, 2], [1, 2], [1, 2]]]
expected = 2
```

### Case 3

```python
args = [[[1, 2], [2, 3]]]
expected = 0
```

### Case 4

```python
args = [[[1, 2]]]
expected = 0
```

### Case 5

```python
args = [[[1, 2], [1, 3], [2, 3], [3, 4]]]
expected = 1
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run non-overlapping-intervals
```
