# 083. Walls And Gates

- Chapter: 11. Graphs
- Difficulty: Medium
- Source: https://leetcode.com/problems/walls-and-gates/
- Reference: https://neetcode.io/problems/islands-and-treasure?list=neetcode150

## Goal

Classic interview problem for Walls And Gates. Practice DFS/BFS and topological sorting. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: DFS/BFS.
- Before coding, state the invariant or state definition: topological sorting.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: arg1: an integer matrix: rows r, cols c, then r lines of c integers. Output: the matrix: rows r, cols c, then r lines of c integers.

## Local Examples

### Case 1

**Input**

```
4 4
2147483647 -1 0 2147483647
2147483647 2147483647 2147483647 -1
2147483647 -1 2147483647 -1
0 -1 2147483647 2147483647
```

**Output**

```
4 4
3 -1 0 1
2 2 1 -1
1 -1 2 -1
0 -1 3 4
```

### Case 2

**Input**

```
2 2
0 -1
2147483647 2147483647
```

**Output**

```
2 2
0 -1
1 2
```

### Case 3

**Input**

```
1 1
0
```

**Output**

```
1 1
0
```

## Run

```bash
python3 train.py run walls-and-gates
```
