# 049. Same Tree

- Chapter: 07. Trees
- Difficulty: Easy
- Source: https://leetcode.com/problems/same-tree/
- Reference: https://neetcode.io/problems/same-binary-tree?list=neetcode150

## Goal

Classic interview problem for Same Tree. Practice recursive return-value design and DFS/BFS. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: recursive return-value design.
- Before coding, state the invariant or state definition: DFS/BFS.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: p: a binary tree: count n then n level-order values (null for missing); q: a binary tree: count n then n level-order values (null for missing). Output: 1 if true else 0.

## Local Examples

### Case 1

**Input**

```
3
1 2 3
3
1 2 3
```

**Output**

```
1
```

### Case 2

**Input**

```
2
1 2
3
1 null 2
```

**Output**

```
0
```

### Case 3

**Input**

```
3
1 2 1
3
1 1 2
```

**Output**

```
0
```

## Run

```bash
python3 train.py run same-tree
```
