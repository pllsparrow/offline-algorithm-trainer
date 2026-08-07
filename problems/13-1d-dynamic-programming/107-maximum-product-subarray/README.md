# 107. Maximum Product Subarray

- Chapter: 13. 1-D Dynamic Programming
- Difficulty: Medium
- Source: https://leetcode.com/problems/maximum-product-subarray/
- Reference: https://neetcode.io/problems/maximum-product-subarray?list=neetcode150

## Goal

Classic interview problem for Maximum Product Subarray. Practice state definition and transition equations. Start with a brute-force idea, then optimize to an interview-ready complexity.

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
4
2 3 -2 4
```

**Output**

```
6
```

### Case 2

**Input**

```
3
-2 0 -1
```

**Output**

```
0
```

### Case 3

**Input**

```
1
1
```

**Output**

```
1
```

## Run

```bash
python3 train.py run maximum-product-subarray
```
