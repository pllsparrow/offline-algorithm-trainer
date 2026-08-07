# 122. Maximum Subarray

- Chapter: 15. Greedy
- Difficulty: Medium
- Source: https://leetcode.com/problems/maximum-subarray/
- Reference: https://neetcode.io/problems/maximum-subarray?list=neetcode150

## Goal

Find the maximum sum of a contiguous subarray. Practice Kadane's algorithm and local state transitions.

## Interview Focus

- Identify the core pattern: local optimality proofs.
- Before coding, state the invariant or state definition: interval/jump strategies.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: arg1: an integer list: count n then n integers. Output: the integer.

## Local Examples

### Case 1

**Input**

```
9
-2 1 -3 4 -1 2 1 -5 4
```

**Output**

```
6
```

### Case 2

**Input**

```
1
1
```

**Output**

```
1
```

### Case 3

**Input**

```
5
5 4 -1 7 8
```

**Output**

```
23
```

## Run

```bash
python3 train.py run maximum-subarray
```
