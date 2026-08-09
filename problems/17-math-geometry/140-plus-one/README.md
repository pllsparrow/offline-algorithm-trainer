# 140. Plus One

- Chapter: 17. Math & Geometry
- Difficulty: Easy
- Source: https://leetcode.com/problems/plus-one/
- Reference: https://neetcode.io/problems/plus-one?list=neetcode150

## Goal

Classic interview problem for Plus One. Practice in-place matrix operations and simulation. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: in-place matrix operations.
- Before coding, state the invariant or state definition: simulation.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: digits: an integer list: count n then n integers. Output: the values space-separated.

## Local Examples

### Case 1

**Input**

```
3
1 2 3
```

**Output**

```
1 2 4
```

### Case 2

**Input**

```
4
4 3 2 1
```

**Output**

```
4 3 2 2
```

### Case 3

**Input**

```
1
9
```

**Output**

```
1 0
```

## Run

```bash
python3 train.py run plus-one
```
