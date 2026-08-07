# 059. Serialize And Deserialize Binary Tree

- Chapter: 07. Trees
- Difficulty: Hard
- Source: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
- Reference: https://neetcode.io/problems/serialize-and-deserialize-binary-tree?list=neetcode150

## Goal

Classic interview problem for Serialize And Deserialize Binary Tree. Practice recursive return-value design and DFS/BFS. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: recursive return-value design.
- Before coding, state the invariant or state definition: DFS/BFS.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: arg1: a binary tree: count n then n level-order values (null for missing). Output: level-order values space-separated (null for missing).

## Local Examples

### Case 1

**Input**

```
7
1 2 3 null null 4 5
```

**Output**

```
1 2 3 null null 4 5
```

### Case 2

**Input**

```
0

```

**Output**

```
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
python3 train.py run serialize-and-deserialize-binary-tree
```
