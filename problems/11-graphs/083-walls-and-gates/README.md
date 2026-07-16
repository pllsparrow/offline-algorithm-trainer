# 083. Walls And Gates

- Chapter: 11. Graphs
- Difficulty: Medium
- Source: https://leetcode.com/problems/walls-and-gates/
- Reference: https://neetcode.io/problems/islands-and-treasure?list=neetcode150

## Goal

Classic interview problem for Walls And Gates. Practice DFS/BFS and topological sorting. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: DFS/BFS.
- Before coding, state the invariant or state definition: topological sorting.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [[[2147483647, -1, 0, 2147483647], [2147483647, 2147483647, 2147483647, -1], [2147483647, -1, 2147483647, -1], [0, -1, 2147483647, 2147483647]]]
expected = [[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]]
```

### Case 2

```python
args = [[[0, -1], [2147483647, 2147483647]]]
expected = [[0, -1], [1, 2]]
```

### Case 3

```python
args = [[[0]]]
expected = [[0]]
```

### Case 4

```python
args = [[[-1]]]
expected = [[-1]]
```

### Case 5

```python
args = [[[2147483647]]]
expected = [[2147483647]]
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run walls-and-gates
```
