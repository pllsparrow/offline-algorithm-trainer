# 095. Min Cost to Connect All Points

- Chapter: 12. Advanced Graphs
- Difficulty: Medium
- Source: https://leetcode.com/problems/min-cost-to-connect-all-points/
- Reference: https://neetcode.io/problems/min-cost-to-connect-points?list=neetcode150

## Goal

Classic interview problem for Min Cost to Connect All Points. Practice shortest paths and minimum spanning trees. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: shortest paths.
- Before coding, state the invariant or state definition: minimum spanning trees.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: arg1: edges2: count then values. Output: the integer.

## Local Examples

### Case 1

**Input**

```
5
0 0
2 2
3 10
5 2
7 0
```

**Output**

```
20
```

### Case 2

**Input**

```
3
3 12
-2 5
-4 1
```

**Output**

```
18
```

### Case 3

**Input**

```
1
0 0
```

**Output**

```
0
```

## Run

```bash
python3 train.py run min-cost-to-connect-all-points
```
