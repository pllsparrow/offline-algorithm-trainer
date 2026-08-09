# 141. Pow(x, n)

- Chapter: 17. Math & Geometry
- Difficulty: Medium
- Source: https://leetcode.com/problems/powx-n/
- Reference: https://neetcode.io/problems/pow-x-n?list=neetcode150

## Goal

Classic interview problem for Pow(x, n). Practice in-place matrix operations and simulation. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: in-place matrix operations.
- Before coding, state the invariant or state definition: simulation.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: x: a float; n: an integer. Output: the float.

## Local Examples

### Case 1

**Input**

```
2.0
10
```

**Output**

```
1024.0
```

### Case 2

**Input**

```
2.1
3
```

**Output**

```
9.261
```

### Case 3

**Input**

```
2.0
-2
```

**Output**

```
0.25
```

## Run

```bash
python3 train.py run powx-n
```
