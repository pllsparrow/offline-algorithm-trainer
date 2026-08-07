# 052. Binary Tree Level Order Traversal

- Chapter: 07. Trees
- Difficulty: Medium
- Source: https://leetcode.com/problems/binary-tree-level-order-traversal/
- Reference: https://neetcode.io/problems/level-order-traversal-of-binary-tree?list=neetcode150

## Goal

Classic interview problem for Binary Tree Level Order Traversal. Practice recursive return-value design and DFS/BFS. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: recursive return-value design.
- Before coding, state the invariant or state definition: DFS/BFS.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: arg1: a binary tree: count n then n level-order values (null for missing). Output: count m then m lines of pairs.

## Local Examples

### Case 1

**Input**

```
7
3 9 20 null null 15 7
```

**Output**

```
3
3
9 20
15 7
```

### Case 2

**Input**

```
1
1
```

**Output**

```
1
1
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
python3 train.py run binary-tree-level-order-traversal
```
