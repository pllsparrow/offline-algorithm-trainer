# 035. Merge Two Sorted Lists

- Chapter: 06. Linked List
- Difficulty: Easy
- Source: https://leetcode.com/problems/merge-two-sorted-lists/
- Reference: https://neetcode.io/problems/merge-two-sorted-linked-lists?list=neetcode150

## Goal

Classic interview problem for Merge Two Sorted Lists. Practice pointer rewiring and fast and slow pointers. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: pointer rewiring.
- Before coding, state the invariant or state definition: fast and slow pointers.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: list1: an integer list: count n then n integers; list2: an integer list: count n then n integers. Output: the values space-separated.

## Local Examples

### Case 1

**Input**

```
3
1 2 4
3
1 3 4
```

**Output**

```
1 1 2 3 4 4
```

### Case 2

**Input**

```
0

0

```

**Output**

```
```

### Case 3

**Input**

```
0

1
0
```

**Output**

```
0
```

## Run

```bash
python3 train.py run merge-two-sorted-lists
```
