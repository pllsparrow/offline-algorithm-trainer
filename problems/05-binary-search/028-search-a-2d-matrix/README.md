# 028. Search a 2D Matrix

- Chapter: 05. Binary Search
- Difficulty: Medium
- Source: https://leetcode.com/problems/search-a-2d-matrix/
- Reference: https://neetcode.io/problems/search-2d-matrix?list=neetcode150

## Goal

Classic interview problem for Search a 2D Matrix. Practice search space definition and boundary shrinking. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: search space definition.
- Before coding, state the invariant or state definition: boundary shrinking.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: matrix: an integer matrix: rows r, cols c, then r lines of c integers; target: an integer. Output: 1 if true else 0.

## Local Examples

### Case 1

**Input**

```
3 4
1 3 5 7
10 11 16 20
23 30 34 60
3
```

**Output**

```
1
```

### Case 2

**Input**

```
3 4
1 3 5 7
10 11 16 20
23 30 34 60
13
```

**Output**

```
0
```

### Case 3

**Input**

```
3 4
1 3 5 7
10 11 16 20
23 30 34 60
60
```

**Output**

```
1
```

## Run

```bash
python3 train.py run search-a-2d-matrix
```
