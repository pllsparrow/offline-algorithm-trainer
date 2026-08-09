# 040. Add Two Numbers

- Chapter: 06. Linked List
- Difficulty: Medium
- Source: https://leetcode.com/problems/add-two-numbers/
- Reference: https://neetcode.io/problems/add-two-numbers?list=neetcode150

## Goal

Classic interview problem for Add Two Numbers. Practice pointer rewiring and fast and slow pointers. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: pointer rewiring.
- Before coding, state the invariant or state definition: fast and slow pointers.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: l1: an integer list: count n then n integers; l2: an integer list: count n then n integers. Output: the values space-separated.

## Local Examples

### Case 1

**Input**

```
3
2 4 3
3
5 6 4
```

**Output**

```
7 0 8
```

### Case 2

**Input**

```
1
0
1
0
```

**Output**

```
0
```

### Case 3

**Input**

```
7
9 9 9 9 9 9 9
4
9 9 9 9
```

**Output**

```
8 9 9 9 0 0 0 1
```

## Run

```bash
python3 train.py run add-two-numbers
```
