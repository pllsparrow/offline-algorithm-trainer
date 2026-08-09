# 089. Graph Valid Tree

- Chapter: 11. Graphs
- Difficulty: Medium
- Source: https://leetcode.com/problems/graph-valid-tree/
- Reference: https://neetcode.io/problems/valid-tree?list=neetcode150

## Goal

Classic interview problem for Graph Valid Tree. Practice DFS/BFS and topological sorting. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: DFS/BFS.
- Before coding, state the invariant or state definition: topological sorting.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: n: an integer; edges: edges2: count then values. Output: 1 if true else 0.

## Local Examples

### Case 1

**Input**

```
5
4
0 1
0 2
0 3
1 4
```

**Output**

```
1
```

### Case 2

**Input**

```
5
5
0 1
1 2
2 3
1 3
1 4
```

**Output**

```
0
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
python3 train.py run graph-valid-tree
```
