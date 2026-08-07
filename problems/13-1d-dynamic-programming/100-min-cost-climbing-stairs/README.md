# 100. Min Cost Climbing Stairs

- Chapter: 13. 1-D Dynamic Programming
- Difficulty: Easy
- Source: https://leetcode.com/problems/min-cost-climbing-stairs/
- Reference: https://neetcode.io/problems/min-cost-climbing-stairs?list=neetcode150

## Goal

Classic interview problem for Min Cost Climbing Stairs. Practice state definition and transition equations. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: state definition.
- Before coding, state the invariant or state definition: transition equations.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: arg1: an integer list: count n then n integers. Output: the integer.

## Local Examples

### Case 1

**Input**

```
3
10 15 20
```

**Output**

```
15
```

### Case 2

**Input**

```
10
1 100 1 1 1 100 1 1 100 1
```

**Output**

```
6
```

### Case 3

**Input**

```
2
1 2
```

**Output**

```
1
```

## Run

```bash
python3 train.py run min-cost-climbing-stairs
```
