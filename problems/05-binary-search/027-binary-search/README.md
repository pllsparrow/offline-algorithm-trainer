# 027. Binary Search

- Chapter: 05. Binary Search
- Difficulty: Easy
- Source: https://leetcode.com/problems/binary-search/
- Reference: https://neetcode.io/problems/binary-search?list=neetcode150

## Goal

Search for a target in a sorted array. Practice binary-search boundaries.

## Interview Focus

- Identify the core pattern: search space definition.
- Before coding, state the invariant or state definition: boundary shrinking.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [[-1, 0, 3, 5, 9, 12], 9]
expected = 4
```

### Case 2

```python
args = [[-1, 0, 3, 5, 9, 12], 2]
expected = -1
```

### Case 3

```python
args = [[5], 5]
expected = 0
```

### Case 4

```python
args = [[5], -5]
expected = -1
```

### Case 5

```python
args = [[1, 3, 5, 7, 9], 1]
expected = 0
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run binary-search
```
