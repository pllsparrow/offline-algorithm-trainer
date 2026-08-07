# 043. Merge K Sorted Lists

- Chapter: 06. Linked List
- Difficulty: Hard
- Source: https://leetcode.com/problems/merge-k-sorted-lists/
- Reference: https://neetcode.io/problems/merge-k-sorted-linked-lists?list=neetcode150

## Goal

Classic interview problem for Merge K Sorted Lists. Practice pointer rewiring and fast and slow pointers. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: pointer rewiring.
- Before coding, state the invariant or state definition: fast and slow pointers.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: arg1: k linked lists: count k, then per list count n and n integers. Output: the values space-separated.

## Local Examples

### Case 1

**Input**

```
3
3
1 4 5
3
1 3 4
2
2 6
```

**Output**

```
1 1 2 3 4 4 5 6
```

### Case 2

**Input**

```
0
```

**Output**

```
```

### Case 3

**Input**

```
1
0

```

**Output**

```
```

## Run

```bash
python3 train.py run merge-k-sorted-lists
```
