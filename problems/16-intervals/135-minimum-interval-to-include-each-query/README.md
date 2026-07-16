# 135. Minimum Interval to Include Each Query

- Chapter: 16. Intervals
- Difficulty: Hard
- Source: https://leetcode.com/problems/minimum-interval-to-include-each-query/
- Reference: https://neetcode.io/problems/minimum-interval-including-query?list=neetcode150

## Goal

Classic interview problem for Minimum Interval to Include Each Query. Practice sorting then merging and overlap checks. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: sorting then merging.
- Before coding, state the invariant or state definition: overlap checks.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [[[1, 4], [2, 4], [3, 6], [4, 4]], [2, 3, 4, 5]]
expected = [3, 3, 1, 4]
```

### Case 2

```python
args = [[[2, 3], [2, 5], [1, 8], [20, 25]], [2, 19, 5, 22]]
expected = [2, -1, 4, 6]
```

### Case 3

```python
args = [[[1, 5]], [3]]
expected = [5]
```

### Case 4

```python
args = [[[1, 5]], [6]]
expected = [-1]
```

### Case 5

```python
args = [[[1, 1]], [1]]
expected = [1]
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run minimum-interval-to-include-each-query
```
