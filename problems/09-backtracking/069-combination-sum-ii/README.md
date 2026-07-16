# 069. Combination Sum II

- Chapter: 09. Backtracking
- Difficulty: Medium
- Source: https://leetcode.com/problems/combination-sum-ii/
- Reference: https://neetcode.io/problems/combination-target-sum-ii?list=neetcode150

## Goal

Classic interview problem for Combination Sum II. Practice choice paths and pruning. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: choice paths.
- Before coding, state the invariant or state definition: pruning.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [[10, 1, 2, 7, 6, 1, 5], 8]
expected = [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
```

### Case 2

```python
args = [[2, 5, 2, 1, 2], 5]
expected = [[1, 2, 2], [5]]
```

### Case 3

```python
args = [[1], 1]
expected = [[1]]
```

### Case 4

```python
args = [[1], 2]
expected = []
```

### Case 5

```python
args = [[2], 1]
expected = []
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run combination-sum-ii
```
