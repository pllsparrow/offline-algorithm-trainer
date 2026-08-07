# 109. Longest Increasing Subsequence

- Chapter: 13. 1-D Dynamic Programming
- Difficulty: Medium
- Source: https://leetcode.com/problems/longest-increasing-subsequence/
- Reference: https://neetcode.io/problems/longest-increasing-subsequence?list=neetcode150

## Goal

Classic interview problem for Longest Increasing Subsequence. Practice state definition and transition equations. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: state definition.
- Before coding, state the invariant or state definition: transition equations.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: arg1: an integer list: count n then n integers. Output: the integer.

## Local Examples

### Case 1

**Input**

```
8
10 9 2 5 3 7 101 18
```

**Output**

```
4
```

### Case 2

**Input**

```
6
0 1 0 3 2 3
```

**Output**

```
4
```

### Case 3

**Input**

```
7
7 7 7 7 7 7 7
```

**Output**

```
1
```

## Run

```bash
python3 train.py run longest-increasing-subsequence
```
