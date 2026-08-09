# 051. Lowest Common Ancestor of a Binary Search Tree

- Chapter: 07. Trees
- Difficulty: Medium
- Source: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
- Reference: https://neetcode.io/problems/lowest-common-ancestor-in-binary-search-tree?list=neetcode150

## Goal

Classic interview problem for Lowest Common Ancestor of a Binary Search Tree. Practice recursive return-value design and DFS/BFS. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: recursive return-value design.
- Before coding, state the invariant or state definition: DFS/BFS.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: root: a binary tree: count n then n level-order values (null for missing); p: a tree node value (integer); q: a tree node value (integer). Output: the integer.

## Local Examples

### Case 1

**Input**

```
11
6 2 8 0 4 7 9 null null 3 5
2
8
```

**Output**

```
6
```

### Case 2

**Input**

```
11
6 2 8 0 4 7 9 null null 3 5
2
4
```

**Output**

```
2
```

### Case 3

**Input**

```
2
2 1
2
1
```

**Output**

```
2
```

## Run

```bash
python3 train.py run lowest-common-ancestor-of-a-binary-search-tree
```
