# 082. Clone Graph

- Chapter: 11. Graphs
- Difficulty: Medium
- Source: https://leetcode.com/problems/clone-graph/
- Reference: https://neetcode.io/problems/clone-graph?list=neetcode150

## Goal

Classic interview problem for Clone Graph. Practice DFS/BFS and topological sorting. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: DFS/BFS.
- Before coding, state the invariant or state definition: topological sorting.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [[[2, 4], [1, 3], [2, 4], [1, 3]]]
expected = [[2, 4], [1, 3], [2, 4], [1, 3]]
```

### Case 2

```python
args = [[[]]]
expected = [[]]
```

### Case 3

```python
args = [[]]
expected = []
```

### Case 4

```python
args = [[[2], [1]]]
expected = [[2], [1]]
```

### Case 5

```python
args = [[[2, 3], [1], [1]]]
expected = [[2, 3], [1], [1]]
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run clone-graph
```
