# 028. Search a 2D Matrix

- Chapter: 05. Binary Search
- Difficulty: Medium
- Source: https://leetcode.com/problems/search-a-2d-matrix/
- Reference: https://neetcode.io/problems/search-2d-matrix?list=neetcode150

## Goal

Classic interview problem for Search a 2D Matrix. Practice search space definition and boundary shrinking. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: search space definition.
- Before coding, state the invariant or state definition: boundary shrinking.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3]
expected = True
```

### Case 2

```python
args = [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13]
expected = False
```

### Case 3

```python
args = [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 60]
expected = True
```

### Case 4

```python
args = [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 1]
expected = True
```

### Case 5

```python
args = [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 0]
expected = False
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run search-a-2d-matrix
```
