# 014. Trapping Rain Water

- Chapter: 02. Two Pointers
- Difficulty: Hard
- Source: https://leetcode.com/problems/trapping-rain-water/
- Reference: https://neetcode.io/problems/trapping-rain-water?list=neetcode150

## Goal

Classic interview problem for Trapping Rain Water. Practice left/right pointers and sorted array scanning. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: left/right pointers.
- Before coding, state the invariant or state definition: sorted array scanning.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: height: an integer list: count n then n integers. Output: the integer.

## Local Examples

### Case 1

**Input**

```
12
0 1 0 2 1 0 1 3 2 1 2 1
```

**Output**

```
6
```

### Case 2

**Input**

```
6
4 2 0 3 2 5
```

**Output**

```
9
```

### Case 3

**Input**

```
5
3 0 2 0 4
```

**Output**

```
7
```

## Run

```bash
python3 train.py run trapping-rain-water
```
