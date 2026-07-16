# 103. Longest Palindromic Substring

- Chapter: 13. 1-D Dynamic Programming
- Difficulty: Medium
- Source: https://leetcode.com/problems/longest-palindromic-substring/
- Reference: https://neetcode.io/problems/longest-palindromic-substring?list=neetcode150

## Goal

Classic interview problem for Longest Palindromic Substring. Practice state definition and transition equations. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: state definition.
- Before coding, state the invariant or state definition: transition equations.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = ['babad']
expected = ['aba', 'bab']
```

### Case 2

```python
args = ['cbbd']
expected = ['bb']
```

### Case 3

```python
args = ['a']
expected = ['a']
```

### Case 4

```python
args = ['ac']
expected = ['a', 'c']
```

### Case 5

```python
args = ['racecar']
expected = ['racecar']
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run longest-palindromic-substring
```
