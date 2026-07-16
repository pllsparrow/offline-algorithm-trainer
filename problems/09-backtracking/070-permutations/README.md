# 070. Permutations

- Chapter: 09. Backtracking
- Difficulty: Medium
- Source: https://leetcode.com/problems/permutations/
- Reference: https://neetcode.io/problems/permutations?list=neetcode150

## Goal

Classic interview problem for Permutations. Practice choice paths and pruning. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: choice paths.
- Before coding, state the invariant or state definition: pruning.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [[1, 2, 3]]
expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
```

### Case 2

```python
args = [[0, 1]]
expected = [[0, 1], [1, 0]]
```

### Case 3

```python
args = [[1]]
expected = [[1]]
```

### Case 4

```python
args = [[2, 1]]
expected = [[2, 1], [1, 2]]
```

### Case 5

```python
args = [[0]]
expected = [[0]]
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run permutations
```
