# 114. Coin Change II

- Chapter: 14. 2-D Dynamic Programming
- Difficulty: Medium
- Source: https://leetcode.com/problems/coin-change-ii/
- Reference: https://neetcode.io/problems/coin-change-ii?list=neetcode150

## Goal

Classic interview problem for Coin Change II. Practice 2D state design and string DP. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: 2D state design.
- Before coding, state the invariant or state definition: string DP.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: amount: an integer; coins: an integer list: count n then n integers. Output: the integer.

## Local Examples

### Case 1

**Input**

```
5
3
1 2 5
```

**Output**

```
4
```

### Case 2

**Input**

```
3
1
2
```

**Output**

```
0
```

### Case 3

**Input**

```
10
1
10
```

**Output**

```
1
```

## Run

```bash
python3 train.py run coin-change-ii
```
