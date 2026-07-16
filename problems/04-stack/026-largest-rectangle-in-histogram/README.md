# 026. Largest Rectangle In Histogram

- Chapter: 04. Stack
- Difficulty: Hard
- Source: https://leetcode.com/problems/largest-rectangle-in-histogram/
- Reference: https://neetcode.io/problems/largest-rectangle-in-histogram?list=neetcode150

## Goal

Classic interview problem for Largest Rectangle In Histogram. Practice monotonic stacks and parentheses matching. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: monotonic stacks.
- Before coding, state the invariant or state definition: parentheses matching.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [[2, 1, 5, 6, 2, 3]]
expected = 10
```

### Case 2

```python
args = [[2, 4]]
expected = 4
```

### Case 3

```python
args = [[1]]
expected = 1
```

### Case 4

```python
args = [[0]]
expected = 0
```

### Case 5

```python
args = [[1, 1]]
expected = 2
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run largest-rectangle-in-histogram
```
