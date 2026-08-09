# 086. Surrounded Regions

- Chapter: 11. Graphs
- Difficulty: Medium
- Source: https://leetcode.com/problems/surrounded-regions/
- Reference: https://neetcode.io/problems/surrounded-regions?list=neetcode150

## Goal

Classic interview problem for Surrounded Regions. Practice DFS/BFS and topological sorting. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: DFS/BFS.
- Before coding, state the invariant or state definition: topological sorting.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: board: a char board: rows r, cols c, then r lines of c chars. Output: count m then m lines of pairs.

## Local Examples

### Case 1

**Input**

```
4 4
X X X X
X O O X
X X O X
X O X X
```

**Output**

```
4 4
X X X X
X X X X
X X X X
X O X X
```

### Case 2

**Input**

```
1 1
X
```

**Output**

```
1 1
X
```

### Case 3

**Input**

```
1 1
O
```

**Output**

```
1 1
O
```

## Run

```bash
python3 train.py run surrounded-regions
```
