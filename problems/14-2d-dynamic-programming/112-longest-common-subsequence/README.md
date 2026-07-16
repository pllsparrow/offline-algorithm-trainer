# 112. Longest Common Subsequence

- Chapter: 14. 2-D Dynamic Programming
- Difficulty: Medium
- Source: https://leetcode.com/problems/longest-common-subsequence/
- Reference: https://neetcode.io/problems/longest-common-subsequence?list=neetcode150

## Goal

Classic interview problem for Longest Common Subsequence. Practice 2D state design and string DP. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: 2D state design.
- Before coding, state the invariant or state definition: string DP.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = ['abcde', 'ace']
expected = 3
```

### Case 2

```python
args = ['abc', 'abc']
expected = 3
```

### Case 3

```python
args = ['abc', 'def']
expected = 0
```

### Case 4

```python
args = ['', '']
expected = 0
```

### Case 5

```python
args = ['a', 'a']
expected = 1
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run longest-common-subsequence
```
