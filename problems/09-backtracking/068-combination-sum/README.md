# 068. Combination Sum

- Chapter: 09. Backtracking
- Difficulty: Medium
- Source: https://leetcode.com/problems/combination-sum/
- Reference: https://neetcode.io/problems/combination-target-sum?list=neetcode150

## Goal

Classic interview problem for Combination Sum. Practice choice paths and pruning. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: choice paths.
- Before coding, state the invariant or state definition: pruning.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [[2, 3, 6, 7], 7]
expected = [[2, 2, 3], [7]]
```

### Case 2

```python
args = [[2, 3, 5], 8]
expected = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
```

### Case 3

```python
args = [[2], 1]
expected = []
```

### Case 4

```python
args = [[2, 3], 1]
expected = []
```

### Case 5

```python
args = [[3, 5], 3]
expected = [[3]]
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run combination-sum
```
