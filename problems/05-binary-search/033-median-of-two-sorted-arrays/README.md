# 033. Median of Two Sorted Arrays

- Chapter: 05. Binary Search
- Difficulty: Hard
- Source: https://leetcode.com/problems/median-of-two-sorted-arrays/
- Reference: https://neetcode.io/problems/median-of-two-sorted-arrays?list=neetcode150

## Goal

Classic interview problem for Median of Two Sorted Arrays. Practice search space definition and boundary shrinking. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: search space definition.
- Before coding, state the invariant or state definition: boundary shrinking.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: arg1: an integer list: count n then n integers; arg2: an integer list: count n then n integers. Output: the float.

## Local Examples

### Case 1

**Input**

```
2
1 3
1
2
```

**Output**

```
2.0
```

### Case 2

**Input**

```
2
1 2
2
3 4
```

**Output**

```
2.5
```

### Case 3

**Input**

```
1
1
0

```

**Output**

```
1.0
```

## Run

```bash
python3 train.py run median-of-two-sorted-arrays
```
