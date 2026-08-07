# 057. Construct Binary Tree From Preorder And Inorder Traversal

- Chapter: 07. Trees
- Difficulty: Medium
- Source: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
- Reference: https://neetcode.io/problems/binary-tree-from-preorder-and-inorder-traversal?list=neetcode150

## Goal

Classic interview problem for Construct Binary Tree From Preorder And Inorder Traversal. Practice recursive return-value design and DFS/BFS. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: recursive return-value design.
- Before coding, state the invariant or state definition: DFS/BFS.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: arg1: an integer list: count n then n integers; arg2: an integer list: count n then n integers. Output: print nothing.

## Local Examples

### Case 1

**Input**

```
0

0

```

**Output**

```
```

### Case 2

**Input**

```
1
1
1
1
```

**Output**

```
1
```

### Case 3

**Input**

```
5
3 9 20 15 7
5
9 3 15 20 7
```

**Output**

```
3 9 20 null null 15 7
```

## Run

```bash
python3 train.py run construct-binary-tree-from-preorder-and-inorder-traversal
```
