# 024. Daily Temperatures

- Chapter: 04. Stack
- Difficulty: Medium
- Source: https://leetcode.com/problems/daily-temperatures/
- Reference: https://neetcode.io/problems/daily-temperatures?list=neetcode150

## Goal

Classic interview problem for Daily Temperatures. Practice monotonic stacks and parentheses matching. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: monotonic stacks.
- Before coding, state the invariant or state definition: parentheses matching.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: temperatures: an integer list: count n then n integers. Output: the values space-separated.

## Local Examples

### Case 1

**Input**

```
8
73 74 75 71 69 72 76 73
```

**Output**

```
1 1 4 2 1 1 0 0
```

### Case 2

**Input**

```
4
30 40 50 60
```

**Output**

```
1 1 1 0
```

### Case 3

**Input**

```
3
30 60 90
```

**Output**

```
1 1 0
```

## Run

```bash
python3 train.py run daily-temperatures
```
