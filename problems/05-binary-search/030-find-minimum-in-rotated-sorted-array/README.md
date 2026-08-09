# 030. Find Minimum In Rotated Sorted Array

- Chapter: 05. Binary Search
- Difficulty: Medium
- Source: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
- Reference: https://neetcode.io/problems/find-minimum-in-rotated-sorted-array?list=neetcode150

## Goal

Classic interview problem for Find Minimum In Rotated Sorted Array. Practice search space definition and boundary shrinking. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: search space definition.
- Before coding, state the invariant or state definition: boundary shrinking.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: nums: an integer list: count n then n integers. Output: the integer.

## Local Examples

### Case 1

**Input**

```
5
3 4 5 1 2
```

**Output**

```
1
```

### Case 2

**Input**

```
7
4 5 6 7 0 1 2
```

**Output**

```
0
```

### Case 3

**Input**

```
4
11 13 15 17
```

**Output**

```
11
```

## Run

```bash
python3 train.py run find-minimum-in-rotated-sorted-array
```
