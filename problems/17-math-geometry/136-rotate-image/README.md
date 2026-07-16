# 136. Rotate Image

- Chapter: 17. Math & Geometry
- Difficulty: Medium
- Source: https://leetcode.com/problems/rotate-image/
- Reference: https://neetcode.io/problems/rotate-matrix?list=neetcode150

## Goal

Classic interview problem for Rotate Image. Practice in-place matrix operations and simulation. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: in-place matrix operations.
- Before coding, state the invariant or state definition: simulation.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]]
expected = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
```

### Case 2

```python
args = [[[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]]
expected = [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
```

### Case 3

```python
args = [[[1]]]
expected = [[1]]
```

### Case 4

```python
args = [[[1, 2], [3, 4]]]
expected = [[3, 1], [4, 2]]
```

### Case 5

```python
args = [[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]]
expected = [[21, 16, 11, 6, 1], [22, 17, 12, 7, 2], [23, 18, 13, 8, 3], [24, 19, 14, 9, 4], [25, 20, 15, 10, 5]]
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run rotate-image
```
