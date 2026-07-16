# 109. Longest Increasing Subsequence

- Chapter: 13. 1-D Dynamic Programming
- Difficulty: Medium
- Source: https://leetcode.com/problems/longest-increasing-subsequence/
- Reference: https://neetcode.io/problems/longest-increasing-subsequence?list=neetcode150

## Goal

Classic interview problem for Longest Increasing Subsequence. Practice state definition and transition equations. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: state definition.
- Before coding, state the invariant or state definition: transition equations.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [[10, 9, 2, 5, 3, 7, 101, 18]]
expected = 4
```

### Case 2

```python
args = [[0, 1, 0, 3, 2, 3]]
expected = 4
```

### Case 3

```python
args = [[7, 7, 7, 7, 7, 7, 7]]
expected = 1
```

### Case 4

```python
args = [[1, 3, 6, 7, 9, 4, 10, 5, 6]]
expected = 6
```

### Case 5

```python
args = [[10, 22, 9, 33, 21, 50, 41, 60]]
expected = 5
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run longest-increasing-subsequence
```
