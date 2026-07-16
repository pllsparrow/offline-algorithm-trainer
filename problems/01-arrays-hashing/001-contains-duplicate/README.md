# 001. Contains Duplicate

- Chapter: 01. Arrays & Hashing
- Difficulty: Easy
- Source: https://leetcode.com/problems/contains-duplicate/
- Reference: https://neetcode.io/problems/duplicate-integer?list=neetcode150

## Goal

Determine whether an array contains any duplicate value. This is a starter problem for set-based deduplication.

## Interview Focus

- Identify the core pattern: hash table modeling.
- Before coding, state the invariant or state definition: frequency counting.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [[1, 2, 3, 1]]
expected = True
```

### Case 2

```python
args = [[1, 2, 3, 4]]
expected = False
```

### Case 3

```python
args = [[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]]
expected = True
```

### Case 4

```python
args = [[1]]
expected = False
```

### Case 5

```python
args = [[1, 1]]
expected = True
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run contains-duplicate
```
