# 050. Subtree of Another Tree

- Chapter: 07. Trees
- Difficulty: Easy
- Source: https://leetcode.com/problems/subtree-of-another-tree/
- Reference: https://neetcode.io/problems/subtree-of-a-binary-tree?list=neetcode150

## Goal

Classic interview problem for Subtree of Another Tree. Practice recursive return-value design and DFS/BFS. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: recursive return-value design.
- Before coding, state the invariant or state definition: DFS/BFS.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: root: a binary tree: count n then n level-order values (null for missing); sub_root: a binary tree: count n then n level-order values (null for missing). Output: 1 if true else 0.

## Local Examples

### Case 1

**Input**

```
5
3 4 5 1 2
3
4 1 2
```

**Output**

```
1
```

### Case 2

**Input**

```
10
3 4 5 1 2 null null null null 0
3
4 1 2
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
1
1
```

**Output**

```
1
```

## Run

```bash
python3 train.py run subtree-of-another-tree
```
