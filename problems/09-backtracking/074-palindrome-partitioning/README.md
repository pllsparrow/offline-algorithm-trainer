# 074. Palindrome Partitioning

- Chapter: 09. Backtracking
- Difficulty: Medium
- Source: https://leetcode.com/problems/palindrome-partitioning/
- Reference: https://neetcode.io/problems/palindrome-partitioning?list=neetcode150

## Goal

Classic interview problem for Palindrome Partitioning. Practice choice paths and pruning. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: choice paths.
- Before coding, state the invariant or state definition: pruning.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = ['aab']
expected = [['a', 'a', 'b'], ['aa', 'b']]
```

### Case 2

```python
args = ['a']
expected = [['a']]
```

### Case 3

```python
args = ['ab']
expected = [['a', 'b']]
```

### Case 4

```python
args = ['aa']
expected = [['a', 'a'], ['aa']]
```

### Case 5

```python
args = ['abc']
expected = [['a', 'b', 'c']]
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run palindrome-partitioning
```
