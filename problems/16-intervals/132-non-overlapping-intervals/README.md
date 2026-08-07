# 132. Non Overlapping Intervals

- Chapter: 16. Intervals
- Difficulty: Medium
- Source: https://leetcode.com/problems/non-overlapping-intervals/
- Reference: https://neetcode.io/problems/non-overlapping-intervals?list=neetcode150

## Goal

Classic interview problem for Non Overlapping Intervals. Practice sorting then merging and overlap checks. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: sorting then merging.
- Before coding, state the invariant or state definition: overlap checks.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: arg1: edges2: count then values. Output: the integer.

## Local Examples

### Case 1

**Input**

```
4
1 2
2 3
3 4
1 3
```

**Output**

```
1
```

### Case 2

**Input**

```
3
1 2
1 2
1 2
```

**Output**

```
2
```

### Case 3

**Input**

```
2
1 2
2 3
```

**Output**

```
0
```

## Run

```bash
python3 train.py run non-overlapping-intervals
```
