# 084. Rotting Oranges

- Chapter: 11. Graphs
- Difficulty: Medium
- Source: https://leetcode.com/problems/rotting-oranges/
- Reference: https://neetcode.io/problems/rotting-fruit?list=neetcode150

## Goal

Classic interview problem for Rotting Oranges. Practice DFS/BFS and topological sorting. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: DFS/BFS.
- Before coding, state the invariant or state definition: topological sorting.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: arg1: an integer matrix: rows r, cols c, then r lines of c integers. Output: the integer.

## Local Examples

### Case 1

**Input**

```
3 3
2 1 1
1 1 0
0 1 1
```

**Output**

```
4
```

### Case 2

**Input**

```
3 3
2 1 1
0 1 1
1 0 1
```

**Output**

```
-1
```

### Case 3

**Input**

```
1 2
0 2
```

**Output**

```
0
```

## Run

```bash
python3 train.py run rotting-oranges
```
