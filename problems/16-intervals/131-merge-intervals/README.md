# 131. Merge Intervals

- Chapter: 16. Intervals
- Difficulty: Medium
- Source: https://leetcode.com/problems/merge-intervals/
- Reference: https://neetcode.io/problems/merge-intervals?list=neetcode150

## Goal

Classic interview problem for Merge Intervals. Practice sorting then merging and overlap checks. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: sorting then merging.
- Before coding, state the invariant or state definition: overlap checks.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [[[1, 3], [2, 6], [8, 10], [15, 18]]]
expected = [[1, 6], [8, 10], [15, 18]]
```

### Case 2

```python
args = [[[1, 4], [4, 5]]]
expected = [[1, 5]]
```

### Case 3

```python
args = [[[4, 7], [1, 4]]]
expected = [[1, 7]]
```

### Case 4

```python
args = [[[1, 3]]]
expected = [[1, 3]]
```

### Case 5

```python
args = [[[1, 4], [2, 3]]]
expected = [[1, 4]]
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run merge-intervals
```
