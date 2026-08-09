# 080. Number of Islands

- Chapter: 11. Graphs
- Difficulty: Medium
- Source: https://leetcode.com/problems/number-of-islands/
- Reference: https://neetcode.io/problems/count-number-of-islands?list=neetcode150

## Goal

Count islands in a grid. Practice DFS/BFS flood fill.

## Interview Focus

- Identify the core pattern: DFS/BFS.
- Before coding, state the invariant or state definition: topological sorting.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: grid: a char board: rows r, cols c, then r lines of c chars. Output: the integer.

## Local Examples

### Case 1

**Input**

```
4 5
1 1 1 1 0
1 1 0 1 0
1 1 0 0 0
0 0 0 0 0
```

**Output**

```
1
```

### Case 2

**Input**

```
4 5
1 1 0 0 0
1 1 0 0 0
0 0 1 0 0
0 0 0 1 1
```

**Output**

```
3
```

### Case 3

**Input**

```
3 5
1 0 1 1 1
1 0 1 0 1
1 1 1 0 1
```

**Output**

```
1
```

## Run

```bash
python3 train.py run number-of-islands
```
