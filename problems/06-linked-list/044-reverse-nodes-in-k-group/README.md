# 044. Reverse Nodes In K Group

- Chapter: 06. Linked List
- Difficulty: Hard
- Source: https://leetcode.com/problems/reverse-nodes-in-k-group/
- Reference: https://neetcode.io/problems/reverse-nodes-in-k-group?list=neetcode150

## Goal

Classic interview problem for Reverse Nodes In K Group. Practice pointer rewiring and fast and slow pointers. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: pointer rewiring.
- Before coding, state the invariant or state definition: fast and slow pointers.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: arg1: an integer list: count n then n integers; arg2: an integer. Output: the values space-separated.

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
2 1 4 3 5
```

### Case 2

**Input**

```
5
1 2 3 4 5
3
```

**Output**

```
3 2 1 4 5
```

### Case 3

**Input**

```
5
1 2 3 4 5
1
```

**Output**

```
1 2 3 4 5
```

## Run

```bash
python3 train.py run reverse-nodes-in-k-group
```
