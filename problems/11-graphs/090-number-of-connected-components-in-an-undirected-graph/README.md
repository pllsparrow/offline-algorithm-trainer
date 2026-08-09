# 090. Number of Connected Components In An Undirected Graph

- Chapter: 11. Graphs
- Difficulty: Medium
- Source: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
- Reference: https://neetcode.io/problems/count-connected-components?list=neetcode150

## Goal

Classic interview problem for Number of Connected Components In An Undirected Graph. Practice DFS/BFS and topological sorting. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: DFS/BFS.
- Before coding, state the invariant or state definition: topological sorting.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: n: an integer; edges: edges2: count then values. Output: the integer.

## Local Examples

### Case 1

**Input**

```
5
3
0 1
1 2
3 4
```

**Output**

```
2
```

### Case 2

**Input**

```
5
4
0 1
1 2
2 3
3 4
```

**Output**

```
1
```

### Case 3

**Input**

```
1
0
```

**Output**

```
1
```

## Run

```bash
python3 train.py run number-of-connected-components-in-an-undirected-graph
```
