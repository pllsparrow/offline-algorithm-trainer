# 002. Valid Anagram

- Chapter: 01. Arrays & Hashing
- Difficulty: Easy
- Source: https://leetcode.com/problems/valid-anagram/
- Reference: https://neetcode.io/problems/is-anagram?list=neetcode150

## Goal

Determine whether two strings contain the same characters with the same counts. Practice character frequency counting.

## Interview Focus

- Identify the core pattern: hash table modeling.
- Before coding, state the invariant or state definition: frequency counting.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = ['anagram', 'nagaram']
expected = True
```

### Case 2

```python
args = ['rat', 'car']
expected = False
```

### Case 3

```python
args = ['listen', 'silent']
expected = True
```

### Case 4

```python
args = ['hello', 'bello']
expected = False
```

### Case 5

```python
args = ['', '']
expected = True
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run valid-anagram
```
