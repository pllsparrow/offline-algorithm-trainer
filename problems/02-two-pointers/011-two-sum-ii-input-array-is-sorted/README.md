# 011. Two Sum II Input Array Is Sorted

- Chapter: 02. Two Pointers
- Difficulty: Medium
- Source: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
- Reference: https://neetcode.io/problems/two-integer-sum-ii?list=neetcode150

## Goal

Classic interview problem for Two Sum II Input Array Is Sorted. Practice left/right pointers and sorted array scanning. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: left/right pointers.
- Before coding, state the invariant or state definition: sorted array scanning.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: arg1: an integer list: count n then n integers; arg2: an integer. Output: the values space-separated.

## Local Examples

### Case 1

**Input**

```
4
2 7 11 15
9
```

**Output**

```
1 2
```

### Case 2

**Input**

```
3
2 3 4
6
```

**Output**

```
1 3
```

### Case 3

**Input**

```
2
-1 0
-1
```

**Output**

```
1 2
```

## Run

```bash
python3 train.py run two-sum-ii-input-array-is-sorted
```
