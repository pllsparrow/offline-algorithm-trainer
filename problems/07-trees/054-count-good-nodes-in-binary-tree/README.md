# 054. Count Good Nodes In Binary Tree

- Chapter: 07. Trees
- Difficulty: Medium
- Source: https://leetcode.com/problems/count-good-nodes-in-binary-tree/
- Reference: https://neetcode.io/problems/count-good-nodes-in-binary-tree?list=neetcode150

## Goal

Classic interview problem for Count Good Nodes In Binary Tree. Practice recursive return-value design and DFS/BFS. Start with a brute-force idea, then optimize to an interview-ready complexity.

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
7
3 1 4 3 null 1 5
```

**Output**

```
4
```

### Case 2

**Input**

```
5
3 3 null 4 2
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
```

**Output**

```
1
```

## Run

```bash
python3 train.py run count-good-nodes-in-binary-tree
```
