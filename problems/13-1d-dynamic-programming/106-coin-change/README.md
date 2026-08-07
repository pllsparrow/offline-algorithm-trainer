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

## ACM Format

Input: arg1: an integer list: count n then n integers; arg2: an integer. Output: the integer.

## Local Examples

### Case 1

**Input**

```
3
1 2 5
11
```

**Output**

```
3
```

### Case 2

**Input**

```
1
2
3
```

**Output**

```
-1
```

### Case 3

**Input**

```
1
1
0
```

**Output**

```
0
```

## Run

```bash
python3 train.py run coin-change
```
