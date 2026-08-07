# 038. Remove Nth Node From End of List

- Chapter: 06. Linked List
- Difficulty: Medium
- Source: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
- Reference: https://neetcode.io/problems/remove-node-from-end-of-linked-list?list=neetcode150

## Goal

Classic interview problem for Remove Nth Node From End of List. Practice pointer rewiring and fast and slow pointers. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: pointer rewiring.
- Before coding, state the invariant or state definition: fast and slow pointers.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: arg1: a linked list: count n then n integers; arg2: an integer. Output: the values space-separated.

## Local Examples

### Case 1

**Input**

```
5
1 2 3 4 5
2
```

**Output**

```
1 2 3 5
```

### Case 2

**Input**

```
1
1
1
```

**Output**

```
```

### Case 3

**Input**

```
2
1 2
1
```

**Output**

```
1
```

## Run

```bash
python3 train.py run remove-nth-node-from-end-of-list
```
