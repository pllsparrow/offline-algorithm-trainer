# 091. Redundant Connection

- Chapter: 11. Graphs
- Difficulty: Medium
- Source: https://leetcode.com/problems/redundant-connection/
- Reference: https://neetcode.io/problems/redundant-connection?list=neetcode150

## Goal

Classic interview problem for Redundant Connection. Practice DFS/BFS and topological sorting. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: DFS/BFS.
- Before coding, state the invariant or state definition: topological sorting.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [[[1, 2], [1, 3], [2, 3]]]
expected = [2, 3]
```

### Case 2

```python
args = [[[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]]
expected = [1, 4]
```

### Case 3

```python
args = [[[1, 2], [2, 3], [1, 3]]]
expected = [1, 3]
```

### Case 4

```python
args = [[[1, 2], [2, 3], [3, 4], [2, 4], [1, 5]]]
expected = [2, 4]
```

### Case 5

```python
args = [[[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]]
expected = [1, 5]
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run redundant-connection
```
