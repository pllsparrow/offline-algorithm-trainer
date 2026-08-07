# 053. Binary Tree Right Side View

- Chapter: 07. Trees
- Difficulty: Medium
- Source: https://leetcode.com/problems/binary-tree-right-side-view/
- Reference: https://neetcode.io/problems/binary-tree-right-side-view?list=neetcode150

## Goal

Classic interview problem for Binary Tree Right Side View. Practice recursive return-value design and DFS/BFS. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: recursive return-value design.
- Before coding, state the invariant or state definition: DFS/BFS.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: arg1: a binary tree: count n then n level-order values (null for missing). Output: the values space-separated.

## Local Examples

### Case 1

**Input**

```
7
1 2 3 null 5 null 4
```

**Output**

```
1 3 4
```

### Case 2

**Input**

```
8
1 2 3 4 null null null 5
```

**Output**

```
1 3 4 5
```

### Case 3

**Input**

```
3
1 null 3
```

**Output**

```
1 3
```

## Run

```bash
python3 train.py run binary-tree-right-side-view
```
