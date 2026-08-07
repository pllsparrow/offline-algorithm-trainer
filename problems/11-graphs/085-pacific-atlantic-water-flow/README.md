# 085. Pacific Atlantic Water Flow

- Chapter: 11. Graphs
- Difficulty: Medium
- Source: https://leetcode.com/problems/pacific-atlantic-water-flow/
- Reference: https://neetcode.io/problems/pacific-atlantic-water-flow?list=neetcode150

## Goal

Classic interview problem for Pacific Atlantic Water Flow. Practice DFS/BFS and topological sorting. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: DFS/BFS.
- Before coding, state the invariant or state definition: topological sorting.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: arg1: an integer matrix: rows r, cols c, then r lines of c integers. Output: each group on its own line (sorted; each group sorted).

## Local Examples

### Case 1

**Input**

```
5 5
1 2 2 3 5
3 2 3 4 4
2 4 5 3 1
6 7 1 4 5
5 1 1 2 4
```

**Output**

```
0 3
0 4
0 4
1 3
1 3
1 4
2 2
```

### Case 2

**Input**

```
1 1
1
```

**Output**

```
0 0
```

### Case 3

**Input**

```
2 2
2 1
1 2
```

**Output**

```
0 0
0 1
0 1
1 1
```

## Run

```bash
python3 train.py run pacific-atlantic-water-flow
```
