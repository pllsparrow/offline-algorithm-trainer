# 008. Valid Sudoku

- Chapter: 01. Arrays & Hashing
- Difficulty: Medium
- Source: https://leetcode.com/problems/valid-sudoku/
- Reference: https://neetcode.io/problems/valid-sudoku?list=neetcode150

## Goal

Classic interview problem for Valid Sudoku. Practice hash table modeling and frequency counting. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: hash table modeling.
- Before coding, state the invariant or state definition: frequency counting.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: arg1: a char board: rows r, cols c, then r lines of c chars. Output: 1 if true else 0.

## Local Examples

### Case 1

**Input**

```
9 9
5 3 . . 7 . . . .
6 . . 1 9 5 . . .
. 9 8 . . . . 6 .
8 . . . 6 . . . 3
4 . . 8 . 3 . . 1
7 . . . 2 . . . 6
. 6 . . . . 2 8 .
. . . 4 1 9 . . 5
. . . . 8 . . 7 9
```

**Output**

```
1
```

### Case 2

**Input**

```
9 9
8 3 . . 7 . . . .
6 . . 1 9 5 . . .
. 9 8 . . . . 6 .
8 . . . 6 . . . 3
4 . . 8 . 3 . . 1
7 . . . 2 . . . 6
. 6 . . . . 2 8 .
. . . 4 1 9 . . 5
. . . . 8 . . 7 9
```

**Output**

```
0
```

### Case 3

**Input**

```
9 9
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
```

**Output**

```
1
```

## Run

```bash
python3 train.py run valid-sudoku
```
