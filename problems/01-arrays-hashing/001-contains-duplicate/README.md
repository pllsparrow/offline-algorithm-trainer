# 001. Contains Duplicate

- Chapter: 01. Arrays & Hashing
- Difficulty: Easy
- Source: https://leetcode.com/problems/contains-duplicate/
- Reference: https://neetcode.io/problems/duplicate-integer?list=neetcode150

## Goal

Determine whether an array contains any duplicate value. This is a starter problem for set-based deduplication.

## Interview Focus

- Identify the core pattern: hash table modeling.
- Before coding, state the invariant or state definition: frequency counting.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: nums: an integer list: count n then n integers. Output: 1 if true else 0.

## Local Examples

### Case 1

**Input**

```
4
1 2 3 1
```

**Output**

```
1
```

### Case 2

**Input**

```
4
1 2 3 4
```

**Output**

```
0
```

### Case 3

**Input**

```
10
1 1 1 3 3 4 3 2 4 2
```

**Output**

```
1
```

## Run

```bash
python3 train.py run contains-duplicate
```
