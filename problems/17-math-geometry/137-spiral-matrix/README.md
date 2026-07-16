# 137. Spiral Matrix

- Chapter: 17. Math & Geometry
- Difficulty: Medium
- Source: https://leetcode.com/problems/spiral-matrix/
- Reference: https://neetcode.io/problems/spiral-matrix?list=neetcode150

## Goal

Classic interview problem for Spiral Matrix. Practice in-place matrix operations and simulation. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: in-place matrix operations.
- Before coding, state the invariant or state definition: simulation.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]]
expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
```

### Case 2

```python
args = [[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]]
expected = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
```

### Case 3

```python
args = [[[1]]]
expected = [1]
```

### Case 4

```python
args = [[[1, 2]]]
expected = [1, 2]
```

### Case 5

```python
args = [[[1], [2]]]
expected = [1, 2]
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run spiral-matrix
```
