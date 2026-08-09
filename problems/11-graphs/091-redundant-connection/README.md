# 091. Redundant Connection

- Chapter: 11. Graphs
- Difficulty: Medium
- Source: https://leetcode.com/problems/redundant-connection/
- Reference: https://neetcode.io/problems/redundant-connection?list=neetcode150

## Goal

Classic interview problem for Redundant Connection. Practice DFS/BFS and topological sorting. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: DFS/BFS.
- Before coding, state the invariant or state definition: topological sorting.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: edges: edges2: count then values. Output: the values space-separated.

## Local Examples

### Case 1

**Input**

```
3
1 2
1 3
2 3
```

**Output**

```
2 3
```

### Case 2

**Input**

```
5
1 2
2 3
3 4
1 4
1 5
```

**Output**

```
1 4
```

### Case 3

**Input**

```
3
1 2
2 3
1 3
```

**Output**

```
1 3
```

## Run

```bash
python3 train.py run redundant-connection
```
