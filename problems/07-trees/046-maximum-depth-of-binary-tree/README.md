# 046. Maximum Depth of Binary Tree

- Chapter: 07. Trees
- Difficulty: Easy
- Source: https://leetcode.com/problems/maximum-depth-of-binary-tree/
- Reference: https://neetcode.io/problems/depth-of-binary-tree?list=neetcode150

## Goal

Classic interview problem for Maximum Depth of Binary Tree. Practice recursive return-value design and DFS/BFS. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: recursive return-value design.
- Before coding, state the invariant or state definition: DFS/BFS.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: root: a binary tree: count n then n level-order values (null for missing). Output: the integer.

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
```

### Case 2

**Input**

```
3
1 null 2
```

**Output**

```
2
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
python3 train.py run maximum-depth-of-binary-tree
```
