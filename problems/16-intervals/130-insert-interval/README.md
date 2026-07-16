# 130. Insert Interval

- Chapter: 16. Intervals
- Difficulty: Medium
- Source: https://leetcode.com/problems/insert-interval/
- Reference: https://neetcode.io/problems/insert-new-interval?list=neetcode150

## Goal

Classic interview problem for Insert Interval. Practice sorting then merging and overlap checks. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: sorting then merging.
- Before coding, state the invariant or state definition: overlap checks.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [[[1, 3], [6, 9]], [2, 5]]
expected = [[1, 5], [6, 9]]
```

### Case 2

```python
args = [[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]]
expected = [[1, 2], [3, 10], [12, 16]]
```

### Case 3

```python
args = [[], [5, 7]]
expected = [[5, 7]]
```

### Case 4

```python
args = [[[1, 5]], [2, 3]]
expected = [[1, 5]]
```

### Case 5

```python
args = [[[1, 5]], [6, 8]]
expected = [[1, 5], [6, 8]]
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run insert-interval
```
