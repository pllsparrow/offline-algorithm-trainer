# 117. Longest Increasing Path In a Matrix

- Chapter: 14. 2-D Dynamic Programming
- Difficulty: Hard
- Source: https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
- Reference: https://neetcode.io/problems/longest-increasing-path-in-matrix?list=neetcode150

## Goal

Classic interview problem for Longest Increasing Path In a Matrix. Practice 2D state design and string DP. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: 2D state design.
- Before coding, state the invariant or state definition: string DP.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: matrix: an integer matrix: rows r, cols c, then r lines of c integers. Output: the integer.

## Local Examples

### Case 1

**Input**

```
3 3
9 9 4
6 6 8
2 1 1
```

**Output**

```
4
```

### Case 2

**Input**

```
3 3
3 4 5
3 2 6
2 2 1
```

**Output**

```
4
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
python3 train.py run longest-increasing-path-in-a-matrix
```
