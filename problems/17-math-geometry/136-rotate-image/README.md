# 136. Rotate Image

- Chapter: 17. Math & Geometry
- Difficulty: Medium
- Source: https://leetcode.com/problems/rotate-image/
- Reference: https://neetcode.io/problems/rotate-matrix?list=neetcode150

## Goal

Classic interview problem for Rotate Image. Practice in-place matrix operations and simulation. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: in-place matrix operations.
- Before coding, state the invariant or state definition: simulation.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: arg1: an integer matrix: rows r, cols c, then r lines of c integers. Output: the matrix: rows r, cols c, then r lines of c integers.

## Local Examples

### Case 1

**Input**

```
3 3
1 2 3
4 5 6
7 8 9
```

**Output**

```
3 3
7 4 1
8 5 2
9 6 3
```

### Case 2

**Input**

```
4 4
5 1 9 11
2 4 8 10
13 3 6 7
15 14 12 16
```

**Output**

```
4 4
15 13 2 5
14 3 4 1
12 6 8 9
16 7 10 11
```

### Case 3

**Input**

```
1 1
1
```

**Output**

```
1 1
1
```

## Run

```bash
python3 train.py run rotate-image
```
