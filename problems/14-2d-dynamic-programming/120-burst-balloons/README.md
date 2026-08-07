# 120. Burst Balloons

- Chapter: 14. 2-D Dynamic Programming
- Difficulty: Hard
- Source: https://leetcode.com/problems/burst-balloons/
- Reference: https://neetcode.io/problems/burst-balloons?list=neetcode150

## Goal

Classic interview problem for Burst Balloons. Practice 2D state design and string DP. Start with a brute-force idea, then optimize to an interview-ready complexity.

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
4
3 1 5 8
```

**Output**

```
167
```

### Case 2

**Input**

```
2
1 5
```

**Output**

```
10
```

### Case 3

**Input**

```
1
5
```

**Output**

```
5
```

## Run

```bash
python3 train.py run burst-balloons
```
