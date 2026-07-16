# 084. Rotting Oranges

- Chapter: 11. Graphs
- Difficulty: Medium
- Source: https://leetcode.com/problems/rotting-oranges/
- Reference: https://neetcode.io/problems/rotting-fruit?list=neetcode150

## Goal

Classic interview problem for Rotting Oranges. Practice DFS/BFS and topological sorting. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: DFS/BFS.
- Before coding, state the invariant or state definition: topological sorting.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [[[2, 1, 1], [1, 1, 0], [0, 1, 1]]]
expected = 4
```

### Case 2

```python
args = [[[2, 1, 1], [0, 1, 1], [1, 0, 1]]]
expected = -1
```

### Case 3

```python
args = [[[0, 2]]]
expected = 0
```

### Case 4

```python
args = [[[0]]]
expected = 0
```

### Case 5

```python
args = [[[1]]]
expected = -1
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run rotting-oranges
```
