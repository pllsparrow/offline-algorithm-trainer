# 015. Best Time to Buy And Sell Stock

- Chapter: 03. Sliding Window
- Difficulty: Easy
- Source: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
- Reference: https://neetcode.io/problems/buy-and-sell-crypto?list=neetcode150

## Goal

Classic interview problem for Best Time to Buy And Sell Stock. Practice window invariants and left/right boundary movement. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: window invariants.
- Before coding, state the invariant or state definition: left/right boundary movement.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: arg1: an integer list: count n then n integers. Output: the integer.

## Local Examples

### Case 1

**Input**

```
6
7 1 5 3 6 4
```

**Output**

```
5
```

### Case 2

**Input**

```
5
7 6 4 3 1
```

**Output**

```
0
```

### Case 3

**Input**

```
5
1 2 3 4 5
```

**Output**

```
4
```

## Run

```bash
python3 train.py run best-time-to-buy-and-sell-stock
```
