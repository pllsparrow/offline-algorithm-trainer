# 096. Swim In Rising Water

- Chapter: 12. Advanced Graphs
- Difficulty: Hard
- Source: https://leetcode.com/problems/swim-in-rising-water/
- Reference: https://neetcode.io/problems/swim-in-rising-water?list=neetcode150

## Goal

Classic interview problem for Swim In Rising Water. Practice shortest paths and minimum spanning trees. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: shortest paths.
- Before coding, state the invariant or state definition: minimum spanning trees.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: grid: an integer matrix: rows r, cols c, then r lines of c integers. Output: the integer.

## Local Examples

### Case 1

**Input**

```
2 2
0 2
1 3
```

**Output**

```
3
```

### Case 2

**Input**

```
5 5
0 1 2 3 4
24 23 22 21 5
12 13 14 15 16
11 17 18 19 20
10 9 8 7 6
```

**Output**

```
16
```

### Case 3

**Input**

```
1 1
0
```

**Output**

```
0
```

## Run

```bash
python3 train.py run swim-in-rising-water
```
