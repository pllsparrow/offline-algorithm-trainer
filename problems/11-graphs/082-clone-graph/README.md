# 082. Clone Graph

- Chapter: 11. Graphs
- Difficulty: Medium
- Source: https://leetcode.com/problems/clone-graph/
- Reference: https://neetcode.io/problems/clone-graph?list=neetcode150

## Goal

Classic interview problem for Clone Graph. Practice DFS/BFS and topological sorting. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: DFS/BFS.
- Before coding, state the invariant or state definition: topological sorting.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: arg1: a graph: count n, then per node degree d and d neighbour ids. Output: count n then n neighbour lists (degree then ids).

## Local Examples

### Case 1

**Input**

```
4
2 2 4
2 1 3
2 2 4
2 1 3
```

**Output**

```
4
2 2 4
2 1 3
2 2 4
2 1 3
```

### Case 2

**Input**

```
1
0
```

**Output**

```
1
0
```

### Case 3

**Input**

```
0
```

**Output**

```
```

## Run

```bash
python3 train.py run clone-graph
```
