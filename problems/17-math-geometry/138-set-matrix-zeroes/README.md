# 138. Set Matrix Zeroes

- Chapter: 17. Math & Geometry
- Difficulty: Medium
- Source: https://leetcode.com/problems/set-matrix-zeroes/
- Reference: https://neetcode.io/problems/set-zeroes-in-matrix?list=neetcode150

## Goal

Classic interview problem for Set Matrix Zeroes. Practice in-place matrix operations and simulation. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: in-place matrix operations.
- Before coding, state the invariant or state definition: simulation.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [[[1, 1, 1], [1, 0, 1], [1, 1, 1]]]
expected = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
```

### Case 2

```python
args = [[[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]]
expected = [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
```

### Case 3

```python
args = [[[1]]]
expected = [[1]]
```

### Case 4

```python
args = [[[0]]]
expected = [[0]]
```

### Case 5

```python
args = [[[1, 0]]]
expected = [[0, 0]]
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run set-matrix-zeroes
```
