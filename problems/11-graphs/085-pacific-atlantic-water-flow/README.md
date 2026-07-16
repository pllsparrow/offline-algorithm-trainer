# 085. Pacific Atlantic Water Flow

- Chapter: 11. Graphs
- Difficulty: Medium
- Source: https://leetcode.com/problems/pacific-atlantic-water-flow/
- Reference: https://neetcode.io/problems/pacific-atlantic-water-flow?list=neetcode150

## Goal

Classic interview problem for Pacific Atlantic Water Flow. Practice DFS/BFS and topological sorting. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: DFS/BFS.
- Before coding, state the invariant or state definition: topological sorting.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [[[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]]
expected = [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
```

### Case 2

```python
args = [[[1]]]
expected = [[0, 0]]
```

### Case 3

```python
args = [[[2, 1], [1, 2]]]
expected = [[0, 0], [0, 1], [1, 0], [1, 1]]
```

### Case 4

```python
args = [[[1, 2, 3], [8, 9, 4], [7, 6, 5]]]
expected = [[0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
```

### Case 5

```python
args = [[[3, 3, 3], [3, 1, 3], [0, 2, 4]]]
expected = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 2], [2, 0], [2, 1], [2, 2]]
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run pacific-atlantic-water-flow
```
