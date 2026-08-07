# 143. Detect Squares

- Chapter: 17. Math & Geometry
- Difficulty: Medium
- Source: https://leetcode.com/problems/detect-squares/
- Reference: https://neetcode.io/problems/count-squares?list=neetcode150

## Goal

Classic interview problem for Detect Squares. Practice in-place matrix operations and simulation. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: in-place matrix operations.
- Before coding, state the invariant or state definition: simulation.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

first line q (operations), then q lines of 'op args...'. Output: one result per operation (null for void; space-separated values for lists)

## Local Examples

### Case 1

**Input**

```
8
DetectSquares
add 2 3 10
add 2 11 2
add 2 3 2
count 2 11 10
count 2 14 8
add 2 11 2
count 2 11 10
```

**Output**

```
null
null
null
null
1
0
null
2
```

### Case 2

**Input**

```
3
DetectSquares
add 2 0 0
count 2 0 0
```

**Output**

```
null
null
0
```

### Case 3

**Input**

```
5
DetectSquares
add 2 0 0
add 2 0 2
add 2 2 0
count 2 2 2
```

**Output**

```
null
null
null
null
1
```

## Run

```bash
python3 train.py run detect-squares
```
