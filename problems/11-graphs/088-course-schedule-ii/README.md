# 088. Course Schedule II

- Chapter: 11. Graphs
- Difficulty: Medium
- Source: https://leetcode.com/problems/course-schedule-ii/
- Reference: https://neetcode.io/problems/course-schedule-ii?list=neetcode150

## Goal

Classic interview problem for Course Schedule II. Practice DFS/BFS and topological sorting. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: DFS/BFS.
- Before coding, state the invariant or state definition: topological sorting.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [2, [[1, 0]]]
expected = [0, 1]
```

### Case 2

```python
args = [4, [[1, 0], [2, 0], [3, 1], [3, 2]]]
expected = [0, 2, 1, 3]
```

### Case 3

```python
args = [1, []]
expected = [0]
```

### Case 4

```python
args = [3, [[1, 0], [2, 1]]]
expected = [0, 1, 2]
```

### Case 5

```python
args = [2, [[1, 0], [0, 1]]]
expected = []
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run course-schedule-ii
```
