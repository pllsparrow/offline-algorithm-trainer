# 003. Two Sum

- Chapter: 01. Arrays & Hashing
- Difficulty: Easy
- Source: https://leetcode.com/problems/two-sum/
- Reference: https://neetcode.io/problems/two-integer-sum?list=neetcode150

## Goal

Find the indices of two numbers whose sum equals the target. Practice looking up complements while traversing with a hash table.

## Interview Focus

- Identify the core pattern: hash table modeling.
- Before coding, state the invariant or state definition: frequency counting.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [[2, 7, 11, 15], 9]
expected = [0, 1]
```

### Case 2

```python
args = [[3, 2, 4], 6]
expected = [1, 2]
```

### Case 3

```python
args = [[3, 3], 6]
expected = [0, 1]
```

### Case 4

```python
args = [[2, 5, 5, 11], 10]
expected = [1, 2]
```

### Case 5

```python
args = [[1, 2, 3, 4, 5], 8]
expected = [2, 4]
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run two-sum
```
