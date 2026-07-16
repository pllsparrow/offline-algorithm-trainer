# 129. Valid Parenthesis String

- Chapter: 15. Greedy
- Difficulty: Medium
- Source: https://leetcode.com/problems/valid-parenthesis-string/
- Reference: https://neetcode.io/problems/valid-parenthesis-string?list=neetcode150

## Goal

Classic interview problem for Valid Parenthesis String. Practice local optimality proofs and interval/jump strategies. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: local optimality proofs.
- Before coding, state the invariant or state definition: interval/jump strategies.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = ['()']
expected = True
```

### Case 2

```python
args = ['(*)']
expected = True
```

### Case 3

```python
args = ['(*))']
expected = True
```

### Case 4

```python
args = ['(']
expected = False
```

### Case 5

```python
args = [')']
expected = False
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run valid-parenthesis-string
```
