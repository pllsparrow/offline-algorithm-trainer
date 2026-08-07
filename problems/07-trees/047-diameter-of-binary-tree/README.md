# 047. Diameter of Binary Tree

- Chapter: 07. Trees
- Difficulty: Easy
- Source: https://leetcode.com/problems/diameter-of-binary-tree/
- Reference: https://neetcode.io/problems/binary-tree-diameter?list=neetcode150

## Goal

Classic interview problem for Diameter of Binary Tree. Practice recursive return-value design and DFS/BFS. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: recursive return-value design.
- Before coding, state the invariant or state definition: DFS/BFS.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: arg1: a binary tree: count n then n level-order values (null for missing). Output: the integer.

## Local Examples

### Case 1

**Input**

```
5
1 2 3 4 5
```

**Output**

```
3
```

### Case 2

**Input**

```
2
1 2
```

**Output**

```
1
```

### Case 3

**Input**

```
0

```

**Output**

```
0
```

## Run

```bash
python3 train.py run diameter-of-binary-tree
```
