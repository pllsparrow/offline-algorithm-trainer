# 037. Reorder List

- Chapter: 06. Linked List
- Difficulty: Medium
- Source: https://leetcode.com/problems/reorder-list/
- Reference: https://neetcode.io/problems/reorder-linked-list?list=neetcode150

## Goal

Classic interview problem for Reorder List. Practice pointer rewiring and fast and slow pointers. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: pointer rewiring.
- Before coding, state the invariant or state definition: fast and slow pointers.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: head: a linked list: count n then n integers. Output: the values space-separated.

## Local Examples

### Case 1

**Input**

```
4
1 2 3 4
```

**Output**

```
1 4 2 3
```

### Case 2

**Input**

```
5
1 2 3 4 5
```

**Output**

```
1 5 2 4 3
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
python3 train.py run reorder-list
```
