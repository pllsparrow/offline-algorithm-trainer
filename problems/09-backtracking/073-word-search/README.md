# 073. Word Search

- Chapter: 09. Backtracking
- Difficulty: Medium
- Source: https://leetcode.com/problems/word-search/
- Reference: https://neetcode.io/problems/search-for-word?list=neetcode150

## Goal

Classic interview problem for Word Search. Practice choice paths and pruning. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: choice paths.
- Before coding, state the invariant or state definition: pruning.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [[['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'ABCCED']
expected = True
```

### Case 2

```python
args = [[['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'SEE']
expected = True
```

### Case 3

```python
args = [[['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'ABCB']
expected = False
```

### Case 4

```python
args = [[['A']], 'A']
expected = True
```

### Case 5

```python
args = [[['A']], 'B']
expected = False
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run word-search
```
