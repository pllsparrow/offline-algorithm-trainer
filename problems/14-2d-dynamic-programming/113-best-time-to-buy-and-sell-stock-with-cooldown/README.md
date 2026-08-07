# 113. Best Time to Buy And Sell Stock With Cooldown

- Chapter: 14. 2-D Dynamic Programming
- Difficulty: Medium
- Source: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
- Reference: https://neetcode.io/problems/buy-and-sell-crypto-with-cooldown?list=neetcode150

## Goal

Classic interview problem for Best Time to Buy And Sell Stock With Cooldown. Practice 2D state design and string DP. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: 2D state design.
- Before coding, state the invariant or state definition: string DP.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: arg1: an integer list: count n then n integers. Output: the integer.

## Local Examples

### Case 1

**Input**

```
5
1 2 3 0 2
```

**Output**

```
3
```

### Case 2

**Input**

```
1
1
```

**Output**

```
0
```

### Case 3

**Input**

```
2
1 2
```

**Output**

```
1
```

## Run

```bash
python3 train.py run best-time-to-buy-and-sell-stock-with-cooldown
```
