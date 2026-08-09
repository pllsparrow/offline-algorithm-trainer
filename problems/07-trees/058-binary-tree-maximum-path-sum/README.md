# 058. Binary Tree Maximum Path Sum

- Chapter: 07. Trees
- Difficulty: Hard
- Source: https://leetcode.com/problems/binary-tree-maximum-path-sum/
- Reference: https://neetcode.io/problems/binary-tree-maximum-path-sum?list=neetcode150

## Goal

Classic interview problem for Binary Tree Maximum Path Sum. Practice recursive return-value design and DFS/BFS. Start with a brute-force idea, then optimize to an interview-ready complexity.

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
3
1 2 3
```

**Output**

```
6
```

### Case 2

**Input**

```
7
-10 9 20 null null 15 7
```

**Output**

```
42
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
python3 train.py run binary-tree-maximum-path-sum
```
