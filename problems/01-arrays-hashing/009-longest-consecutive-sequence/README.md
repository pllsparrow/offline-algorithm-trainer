# 009. Longest Consecutive Sequence

- Chapter: 01. Arrays & Hashing
- Difficulty: Medium
- Source: https://leetcode.com/problems/longest-consecutive-sequence/
- Reference: https://neetcode.io/problems/longest-consecutive-sequence?list=neetcode150

## Goal

Classic interview problem for Longest Consecutive Sequence. Practice hash table modeling and frequency counting. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: hash table modeling.
- Before coding, state the invariant or state definition: frequency counting.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: nums: an integer list: count n then n integers. Output: the integer.

## Local Examples

### Case 1

**Input**

```
6
100 4 200 1 3 2
```

**Output**

```
4
```

### Case 2

**Input**

```
10
0 3 7 2 5 8 4 6 0 1
```

**Output**

```
9
```

### Case 3

**Input**

```
4
1 0 1 2
```

**Output**

```
3
```

## Run

```bash
python3 train.py run longest-consecutive-sequence
```
