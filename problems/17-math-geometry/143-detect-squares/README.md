# 143. Detect Squares

- Chapter: 17. Math & Geometry
- Difficulty: Medium
- Source: https://leetcode.com/problems/detect-squares/
- Reference: https://neetcode.io/problems/count-squares?list=neetcode150

## Goal

Classic interview problem for Detect Squares. Practice in-place matrix operations and simulation. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: in-place matrix operations.
- Before coding, state the invariant or state definition: simulation.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
ops = ['DetectSquares', 'add', 'add', 'add', 'count', 'count', 'add', 'count']
args = [[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11, 10]]]
expected = [None, None, None, None, 1, 0, None, 2]
```

### Case 2

```python
ops = ['DetectSquares', 'add', 'count']
args = [[], [[0, 0]], [[0, 0]]]
expected = [None, None, 0]
```

### Case 3

```python
ops = ['DetectSquares', 'add', 'add', 'add', 'count']
args = [[], [[0, 0]], [[0, 2]], [[2, 0]], [[2, 2]]]
expected = [None, None, None, None, 1]
```

### Case 4

```python
ops = ['DetectSquares', 'add', 'add', 'add', 'add', 'count']
args = [[], [[0, 0]], [[0, 0]], [[0, 2]], [[2, 0]], [[2, 2]]]
expected = [None, None, None, None, None, 2]
```

### Case 5

```python
ops = ['DetectSquares', 'add', 'add', 'add', 'count']
args = [[], [[1, 1]], [[1, 3]], [[3, 1]], [[3, 3]]]
expected = [None, None, None, None, 1]
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run detect-squares
```
