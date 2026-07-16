# 086. Surrounded Regions

- Chapter: 11. Graphs
- Difficulty: Medium
- Source: https://leetcode.com/problems/surrounded-regions/
- Reference: https://neetcode.io/problems/surrounded-regions?list=neetcode150

## Goal

Classic interview problem for Surrounded Regions. Practice DFS/BFS and topological sorting. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: DFS/BFS.
- Before coding, state the invariant or state definition: topological sorting.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [[['X', 'X', 'X', 'X'], ['X', 'O', 'O', 'X'], ['X', 'X', 'O', 'X'], ['X', 'O', 'X', 'X']]]
expected = [['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'O', 'X', 'X']]
```

### Case 2

```python
args = [[['X']]]
expected = [['X']]
```

### Case 3

```python
args = [[['O']]]
expected = [['O']]
```

### Case 4

```python
args = [[['O', 'O'], ['O', 'O']]]
expected = [['O', 'O'], ['O', 'O']]
```

### Case 5

```python
args = [[['X', 'X', 'X'], ['X', 'O', 'X'], ['X', 'X', 'X']]]
expected = [['X', 'X', 'X'], ['X', 'X', 'X'], ['X', 'X', 'X']]
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run surrounded-regions
```
