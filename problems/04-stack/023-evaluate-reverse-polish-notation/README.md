# 023. Evaluate Reverse Polish Notation

- Chapter: 04. Stack
- Difficulty: Medium
- Source: https://leetcode.com/problems/evaluate-reverse-polish-notation/
- Reference: https://neetcode.io/problems/evaluate-reverse-polish-notation?list=neetcode150

## Goal

Classic interview problem for Evaluate Reverse Polish Notation. Practice monotonic stacks and parentheses matching. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: monotonic stacks.
- Before coding, state the invariant or state definition: parentheses matching.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [['2', '1', '+', '3', '*']]
expected = 9
```

### Case 2

```python
args = [['4', '13', '5', '/', '+']]
expected = 6
```

### Case 3

```python
args = [['10', '6', '9', '3', '+', '-11', '*', '/', '*', '17', '+', '5', '+']]
expected = 22
```

### Case 4

```python
args = [['3']]
expected = 3
```

### Case 5

```python
args = [['15', '7', '1', '1', '+', '-', '/', '3', '*', '2', '1', '1', '+', '+', '-']]
expected = 5
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run evaluate-reverse-polish-notation
```
