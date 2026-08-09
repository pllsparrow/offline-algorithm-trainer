# 027. Binary Search

- Chapter: 05. Binary Search
- Difficulty: Easy
- Source: https://leetcode.com/problems/binary-search/
- Reference: https://neetcode.io/problems/binary-search?list=neetcode150

## Goal

Search for a target in a sorted array. Practice binary-search boundaries.

## Interview Focus

- Identify the core pattern: search space definition.
- Before coding, state the invariant or state definition: boundary shrinking.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: nums: an integer list: count n then n integers; target: an integer. Output: the integer.

## Local Examples

### Case 1

**Input**

```
6
-1 0 3 5 9 12
9
```

**Output**

```
4
```

### Case 2

**Input**

```
6
-1 0 3 5 9 12
2
```

**Output**

```
-1
```

### Case 3

**Input**

```
1
5
5
```

**Output**

```
0
```

## Run

```bash
python3 train.py run binary-search
```
