# 039. Copy List With Random Pointer

- Chapter: 06. Linked List
- Difficulty: Medium
- Source: https://leetcode.com/problems/copy-list-with-random-pointer/
- Reference: https://neetcode.io/problems/copy-linked-list-with-random-pointer?list=neetcode150

## Goal

Classic interview problem for Copy List With Random Pointer. Practice pointer rewiring and fast and slow pointers. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: pointer rewiring.
- Before coding, state the invariant or state definition: fast and slow pointers.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: arg1: a random list: count n, then n lines of value and random-index (-1 for null). Output: count n then n lines of value and random-index (-1 for null).

## Local Examples

### Case 1

**Input**

```
5
7 -1
13 0
11 4
10 2
1 0
```

**Output**

```
5
7 -1
13 0
11 4
10 2
1 0
```

### Case 2

**Input**

```
2
1 1
2 1
```

**Output**

```
2
1 1
2 1
```

### Case 3

**Input**

```
3
3 -1
3 0
3 -1
```

**Output**

```
3
3 -1
3 0
3 -1
```

## Run

```bash
python3 train.py run copy-list-with-random-pointer
```
