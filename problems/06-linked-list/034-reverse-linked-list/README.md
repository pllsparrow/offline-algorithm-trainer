# 034. Reverse Linked List

- Chapter: 06. Linked List
- Difficulty: Easy
- Source: https://leetcode.com/problems/reverse-linked-list/
- Reference: https://neetcode.io/problems/reverse-a-linked-list?list=neetcode150

## Goal

Reverse a singly linked list. Practice fundamental pointer rewiring.

## Interview Focus

- Identify the core pattern: pointer rewiring.
- Before coding, state the invariant or state definition: fast and slow pointers.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: arg1: a linked list: count n then n integers. Output: the values space-separated.

## Local Examples

### Case 1

**Input**

```
5
1 2 3 4 5
```

**Output**

```
5 4 3 2 1
```

### Case 2

**Input**

```
2
1 2
```

**Output**

```
2 1
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
python3 train.py run reverse-linked-list
```
