# 021. Valid Parentheses

- Chapter: 04. Stack
- Difficulty: Easy
- Source: https://leetcode.com/problems/valid-parentheses/
- Reference: https://neetcode.io/problems/validate-parentheses?list=neetcode150

## Goal

Classic interview problem for Valid Parentheses. Practice monotonic stacks and parentheses matching. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: monotonic stacks.
- Before coding, state the invariant or state definition: parentheses matching.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = ['()']
expected = True
```

### Case 2

```python
args = ['()[]{}']
expected = True
```

### Case 3

```python
args = ['(]']
expected = False
```

### Case 4

```python
args = ['([])']
expected = True
```

### Case 5

```python
args = ['([)]']
expected = False
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run valid-parentheses
```
