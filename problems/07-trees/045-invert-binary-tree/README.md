# 045. Invert Binary Tree

- Chapter: 07. Trees
- Difficulty: Easy
- Source: https://leetcode.com/problems/invert-binary-tree/
- Reference: https://neetcode.io/problems/invert-a-binary-tree?list=neetcode150

## Goal

Invert a binary tree. Practice recursively processing left and right subtrees.

## Interview Focus

- Identify the core pattern: recursive return-value design.
- Before coding, state the invariant or state definition: DFS/BFS.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: root: a binary tree: count n then n level-order values (null for missing). Output: the values space-separated.

## Local Examples

### Case 1

**Input**

```
7
4 2 7 1 3 6 9
```

**Output**

```
4 7 2 9 6 3 1
```

### Case 2

**Input**

```
3
2 1 3
```

**Output**

```
2 3 1
```

### Case 3

**Input**

```
0

```

**Output**

```
```

## Run

```bash
python3 train.py run invert-binary-tree
```
