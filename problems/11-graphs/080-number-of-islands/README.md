# 080. Number of Islands

- Chapter: 11. Graphs
- Difficulty: Medium
- Source: https://leetcode.com/problems/number-of-islands/
- Reference: https://neetcode.io/problems/count-number-of-islands?list=neetcode150

## Goal

Count islands in a grid. Practice DFS/BFS flood fill.

## Interview Focus

- Identify the core pattern: DFS/BFS.
- Before coding, state the invariant or state definition: topological sorting.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [[['1', '1', '1', '1', '0'], ['1', '1', '0', '1', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '0', '0', '0']]]
expected = 1
```

### Case 2

```python
args = [[['1', '1', '0', '0', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '1', '0', '0'], ['0', '0', '0', '1', '1']]]
expected = 3
```

### Case 3

```python
args = [[['1', '0', '1', '1', '1'], ['1', '0', '1', '0', '1'], ['1', '1', '1', '0', '1']]]
expected = 1
```

### Case 4

```python
args = [[['0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0']]]
expected = 0
```

### Case 5

```python
args = [[['1', '1', '1'], ['0', '1', '0'], ['1', '1', '1']]]
expected = 1
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run number-of-islands
```
