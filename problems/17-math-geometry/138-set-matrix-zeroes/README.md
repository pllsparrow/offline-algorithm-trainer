# 138. Set Matrix Zeroes

- Chapter: 17. Math & Geometry
- Difficulty: Medium
- Source: https://leetcode.com/problems/set-matrix-zeroes/
- Reference: https://neetcode.io/problems/set-zeroes-in-matrix?list=neetcode150

## Goal

Classic interview problem for Set Matrix Zeroes. Practice in-place matrix operations and simulation. Start with a brute-force idea, then optimize to an interview-ready complexity.

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
1 1 1
1 0 1
1 1 1
```

**Output**

```
3 3
1 0 1
0 0 0
1 0 1
```

### Case 2

**Input**

```
3 4
0 1 2 0
3 4 5 2
1 3 1 5
```

**Output**

```
3 4
0 0 0 0
0 4 5 0
0 3 1 0
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
python3 train.py run set-matrix-zeroes
```
