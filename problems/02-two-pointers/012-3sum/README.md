# 012. 3Sum

- Chapter: 02. Two Pointers
- Difficulty: Medium
- Source: https://leetcode.com/problems/3sum/
- Reference: https://neetcode.io/problems/three-integer-sum?list=neetcode150

## Goal

Classic interview problem for 3Sum. Practice left/right pointers and sorted array scanning. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: left/right pointers.
- Before coding, state the invariant or state definition: sorted array scanning.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: arg1: an integer list: count n then n integers. Output: each group on its own line (sorted; each group sorted).

## Local Examples

### Case 1

**Input**

```
6
-1 0 1 2 -1 -4
```

**Output**

```
-1 -1 2
-1 0 1
```

### Case 2

**Input**

```
3
0 1 1
```

**Output**

```
```

### Case 3

**Input**

```
3
0 0 0
```

**Output**

```
0 0 0
```

## Run

```bash
python3 train.py run 3sum
```
