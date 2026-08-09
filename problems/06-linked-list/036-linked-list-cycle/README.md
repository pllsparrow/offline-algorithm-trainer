# 036. Linked List Cycle

- Chapter: 06. Linked List
- Difficulty: Easy
- Source: https://leetcode.com/problems/linked-list-cycle/
- Reference: https://neetcode.io/problems/linked-list-cycle-detection?list=neetcode150

## Goal

Classic interview problem for Linked List Cycle. Practice pointer rewiring and fast and slow pointers. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: pointer rewiring.
- Before coding, state the invariant or state definition: fast and slow pointers.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: head: an integer list: count n then n integers; pos: an integer. Output: 1 if true else 0.

## Local Examples

### Case 1

**Input**

```
4
3 2 0 -4
1
```

**Output**

```
1
```

### Case 2

**Input**

```
2
1 2
0
```

**Output**

```
1
```

### Case 3

**Input**

```
1
1
-1
```

**Output**

```
0
```

## Run

```bash
python3 train.py run linked-list-cycle
```
