# 025. Car Fleet

- Chapter: 04. Stack
- Difficulty: Medium
- Source: https://leetcode.com/problems/car-fleet/
- Reference: https://neetcode.io/problems/car-fleet?list=neetcode150

## Goal

Classic interview problem for Car Fleet. Practice monotonic stacks and parentheses matching. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: monotonic stacks.
- Before coding, state the invariant or state definition: parentheses matching.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: arg1: an integer; arg2: an integer list: count n then n integers; arg3: an integer list: count n then n integers. Output: the integer.

## Local Examples

### Case 1

**Input**

```
12
5
10 8 0 5 3
5
2 4 1 1 3
```

**Output**

```
3
```

### Case 2

**Input**

```
10
1
3
1
3
```

**Output**

```
1
```

### Case 3

**Input**

```
100
3
0 2 4
3
4 2 1
```

**Output**

```
1
```

## Run

```bash
python3 train.py run car-fleet
```
