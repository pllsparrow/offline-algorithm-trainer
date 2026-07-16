# 090. Number of Connected Components In An Undirected Graph

- Chapter: 11. Graphs
- Difficulty: Medium
- Source: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
- Reference: https://neetcode.io/problems/count-connected-components?list=neetcode150

## Goal

Classic interview problem for Number of Connected Components In An Undirected Graph. Practice DFS/BFS and topological sorting. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: DFS/BFS.
- Before coding, state the invariant or state definition: topological sorting.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [5, [[0, 1], [1, 2], [3, 4]]]
expected = 2
```

### Case 2

```python
args = [5, [[0, 1], [1, 2], [2, 3], [3, 4]]]
expected = 1
```

### Case 3

```python
args = [1, []]
expected = 1
```

### Case 4

```python
args = [2, [[0, 1]]]
expected = 1
```

### Case 5

```python
args = [2, []]
expected = 2
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run number-of-connected-components-in-an-undirected-graph
```
