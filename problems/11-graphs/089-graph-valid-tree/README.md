# 089. Graph Valid Tree

- Chapter: 11. Graphs
- Difficulty: Medium
- Source: https://leetcode.com/problems/graph-valid-tree/
- Reference: https://neetcode.io/problems/valid-tree?list=neetcode150

## Goal

Classic interview problem for Graph Valid Tree. Practice DFS/BFS and topological sorting. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: DFS/BFS.
- Before coding, state the invariant or state definition: topological sorting.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [5, [[0, 1], [0, 2], [0, 3], [1, 4]]]
expected = True
```

### Case 2

```python
args = [5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]]
expected = False
```

### Case 3

```python
args = [1, []]
expected = True
```

### Case 4

```python
args = [2, [[0, 1]]]
expected = True
```

### Case 5

```python
args = [2, []]
expected = False
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run graph-valid-tree
```
