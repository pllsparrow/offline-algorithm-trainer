# 024. Daily Temperatures

- Chapter: 04. Stack
- Difficulty: Medium
- Source: https://leetcode.com/problems/daily-temperatures/
- Reference: https://neetcode.io/problems/daily-temperatures?list=neetcode150

## Goal

Classic interview problem for Daily Temperatures. Practice monotonic stacks and parentheses matching. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: monotonic stacks.
- Before coding, state the invariant or state definition: parentheses matching.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [[73, 74, 75, 71, 69, 72, 76, 73]]
expected = [1, 1, 4, 2, 1, 1, 0, 0]
```

### Case 2

```python
args = [[30, 40, 50, 60]]
expected = [1, 1, 1, 0]
```

### Case 3

```python
args = [[30, 60, 90]]
expected = [1, 1, 0]
```

### Case 4

```python
args = [[89, 62, 70, 58, 47, 47, 46, 76, 100, 70]]
expected = [8, 1, 5, 4, 3, 2, 1, 1, 0, 0]
```

### Case 5

```python
args = [[55, 38, 53, 81, 61, 93, 97, 32, 43, 78]]
expected = [3, 1, 1, 2, 1, 1, 0, 1, 1, 0]
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run daily-temperatures
```
