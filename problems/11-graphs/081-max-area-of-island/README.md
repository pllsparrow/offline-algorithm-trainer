# 081. Max Area of Island

- Chapter: 11. Graphs
- Difficulty: Medium
- Source: https://leetcode.com/problems/max-area-of-island/
- Reference: https://neetcode.io/problems/max-area-of-island?list=neetcode150

## Goal

Classic interview problem for Max Area of Island. Practice DFS/BFS and topological sorting. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: DFS/BFS.
- Before coding, state the invariant or state definition: topological sorting.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: grid: an integer matrix: rows r, cols c, then r lines of c integers. Output: the integer.

## Local Examples

### Case 1

**Input**

```
8 13
0 0 1 0 0 0 0 1 0 0 0 0 0
0 0 0 0 0 0 0 1 1 1 0 0 0
0 1 1 0 1 0 0 0 0 0 0 0 0
0 1 0 0 1 1 0 0 1 0 1 0 0
0 1 0 0 1 1 0 0 1 1 1 0 0
0 0 0 0 0 0 0 0 0 0 1 0 0
0 0 0 0 0 0 0 1 1 1 0 0 0
0 0 0 0 0 0 0 1 1 0 0 0 0
```

**Output**

```
6
```

### Case 2

**Input**

```
1 8
0 0 0 0 0 0 0 0
```

**Output**

```
0
```

### Case 3

**Input**

```
1 1
1
```

**Output**

```
1
```

## Run

```bash
python3 train.py run max-area-of-island
```
