# 115. Target Sum

- Chapter: 14. 2-D Dynamic Programming
- Difficulty: Medium
- Source: https://leetcode.com/problems/target-sum/
- Reference: https://neetcode.io/problems/target-sum?list=neetcode150

## Goal

Classic interview problem for Target Sum. Practice 2D state design and string DP. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: 2D state design.
- Before coding, state the invariant or state definition: string DP.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: nums: an integer list: count n then n integers; target: an integer. Output: the integer.

## Local Examples

### Case 1

**Input**

```
5
1 1 1 1 1
3
```

**Output**

```
5
```

### Case 2

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

### Case 3

**Input**

```
1
1
2
```

**Output**

```
0
```

## Run

```bash
python3 train.py run target-sum
```
