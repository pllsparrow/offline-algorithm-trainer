# 063. Kth Largest Element In An Array

- Chapter: 08. Heap / Priority Queue
- Difficulty: Medium
- Source: https://leetcode.com/problems/kth-largest-element-in-an-array/
- Reference: https://neetcode.io/problems/kth-largest-element-in-an-array?list=neetcode150

## Goal

Classic interview problem for Kth Largest Element In An Array. Practice Top K and two heaps. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: Top K.
- Before coding, state the invariant or state definition: two heaps.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: nums: an integer list: count n then n integers; k: an integer. Output: the integer.

## Local Examples

### Case 1

**Input**

```
6
3 2 1 5 6 4
2
```

**Output**

```
5
```

### Case 2

**Input**

```
9
3 2 3 1 2 4 5 5 6
4
```

**Output**

```
4
```

### Case 3

**Input**

```
1
1
1
```

**Output**

```
1
```

## Run

```bash
python3 train.py run kth-largest-element-in-an-array
```
