# 110. Partition Equal Subset Sum

- Chapter: 13. 1-D Dynamic Programming
- Difficulty: Medium
- Source: https://leetcode.com/problems/partition-equal-subset-sum/
- Reference: https://neetcode.io/problems/partition-equal-subset-sum?list=neetcode150

## Goal

Classic interview problem for Partition Equal Subset Sum. Practice state definition and transition equations. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: state definition.
- Before coding, state the invariant or state definition: transition equations.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: nums: an integer list: count n then n integers. Output: 1 if true else 0.

## Local Examples

### Case 1

**Input**

```
4
1 5 11 5
```

**Output**

```
1
```

### Case 2

**Input**

```
4
1 2 3 5
```

**Output**

```
0
```

### Case 3

**Input**

```
2
1 1
```

**Output**

```
1
```

## Run

```bash
python3 train.py run partition-equal-subset-sum
```
