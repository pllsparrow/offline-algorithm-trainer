# 041. Find The Duplicate Number

- Chapter: 06. Linked List
- Difficulty: Medium
- Source: https://leetcode.com/problems/find-the-duplicate-number/
- Reference: https://neetcode.io/problems/find-duplicate-integer?list=neetcode150

## Goal

Classic interview problem for Find The Duplicate Number. Practice pointer rewiring and fast and slow pointers. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: pointer rewiring.
- Before coding, state the invariant or state definition: fast and slow pointers.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: nums: an integer list: count n then n integers. Output: the integer.

## Local Examples

### Case 1

**Input**

```
5
1 3 4 2 2
```

**Output**

```
2
```

### Case 2

**Input**

```
5
3 1 3 4 2
```

**Output**

```
3
```

### Case 3

**Input**

```
5
3 3 3 3 3
```

**Output**

```
3
```

## Run

```bash
python3 train.py run find-the-duplicate-number
```
