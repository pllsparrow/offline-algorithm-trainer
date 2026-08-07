# 056. Kth Smallest Element In a Bst

- Chapter: 07. Trees
- Difficulty: Medium
- Source: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
- Reference: https://neetcode.io/problems/kth-smallest-integer-in-bst?list=neetcode150

## Goal

Classic interview problem for Kth Smallest Element In a Bst. Practice recursive return-value design and DFS/BFS. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: recursive return-value design.
- Before coding, state the invariant or state definition: DFS/BFS.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: arg1: a binary tree: count n then n level-order values (null for missing); arg2: an integer. Output: the integer.

## Local Examples

### Case 1

**Input**

```
5
3 1 4 null 2
1
```

**Output**

```
1
```

### Case 2

**Input**

```
8
5 3 6 2 4 null null 1
3
```

**Output**

```
3
```

### Case 3

**Input**

```
1
1
1
```

**Output**

```
1
```

## Run

```bash
python3 train.py run kth-smallest-element-in-a-bst
```
