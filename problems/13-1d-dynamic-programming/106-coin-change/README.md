# 106. Coin Change

- Chapter: 13. 1-D Dynamic Programming
- Difficulty: Medium
- Source: https://leetcode.com/problems/coin-change/
- Reference: https://neetcode.io/problems/coin-change?list=neetcode150

## Goal

Find the minimum number of coins needed to make a target amount. Practice complete-knapsack DP.

## Interview Focus

- Identify the core pattern: state definition.
- Before coding, state the invariant or state definition: transition equations.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [[1, 2, 5], 11]
expected = 3
```

### Case 2

```python
args = [[2], 3]
expected = -1
```

### Case 3

```python
args = [[1], 0]
expected = 0
```

### Case 4

```python
args = [[1, 3, 4], 6]
expected = 2
```

### Case 5

```python
args = [[2, 5, 10, 1], 27]
expected = 4
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run coin-change
```
