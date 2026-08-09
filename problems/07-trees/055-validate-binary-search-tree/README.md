# 055. Validate Binary Search Tree

- Chapter: 07. Trees
- Difficulty: Medium
- Source: https://leetcode.com/problems/validate-binary-search-tree/
- Reference: https://neetcode.io/problems/valid-binary-search-tree?list=neetcode150

## Goal

Classic interview problem for Validate Binary Search Tree. Practice recursive return-value design and DFS/BFS. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: recursive return-value design.
- Before coding, state the invariant or state definition: DFS/BFS.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: root: a binary tree: count n then n level-order values (null for missing). Output: 1 if true else 0.

## Local Examples

### Case 1

**Input**

```
3
2 1 3
```

**Output**

```
1
```

### Case 2

**Input**

```
7
5 1 4 null null 3 6
```

**Output**

```
0
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
python3 train.py run validate-binary-search-tree
```
