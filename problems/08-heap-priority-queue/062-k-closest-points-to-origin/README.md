# 062. K Closest Points to Origin

- Chapter: 08. Heap / Priority Queue
- Difficulty: Medium
- Source: https://leetcode.com/problems/k-closest-points-to-origin/
- Reference: https://neetcode.io/problems/k-closest-points-to-origin?list=neetcode150

## Goal

Classic interview problem for K Closest Points to Origin. Practice Top K and two heaps. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: Top K.
- Before coding, state the invariant or state definition: two heaps.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [[[1, 3], [-2, 2]], 1]
expected = [[-2, 2]]
```

### Case 2

```python
args = [[[3, 3], [5, -1], [-2, 4]], 2]
expected = [[3, 3], [-2, 4]]
```

### Case 3

```python
args = [[[0, 1], [1, 0]], 2]
expected = [[0, 1], [1, 0]]
```

### Case 4

```python
args = [[[1, 1], [1, 1], [1, 1]], 2]
expected = [[1, 1], [1, 1]]
```

### Case 5

```python
args = [[[0, 0]], 1]
expected = [[0, 0]]
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run k-closest-points-to-origin
```
