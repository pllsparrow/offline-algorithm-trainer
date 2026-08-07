# 135. Minimum Interval to Include Each Query

- Chapter: 16. Intervals
- Difficulty: Hard
- Source: https://leetcode.com/problems/minimum-interval-to-include-each-query/
- Reference: https://neetcode.io/problems/minimum-interval-including-query?list=neetcode150

## Goal

Classic interview problem for Minimum Interval to Include Each Query. Practice sorting then merging and overlap checks. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: sorting then merging.
- Before coding, state the invariant or state definition: overlap checks.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: arg1: edges2: count then values; arg2: an integer list: count n then n integers. Output: the values space-separated.

## Local Examples

### Case 1

**Input**

```
4
1 4
2 4
3 6
4 4
4
2 3 4 5
```

**Output**

```
3 3 1 4
```

### Case 2

**Input**

```
4
2 3
2 5
1 8
20 25
4
2 19 5 22
```

**Output**

```
2 -1 4 6
```

### Case 3

**Input**

```
1
1 5
1
3
```

**Output**

```
5
```

## Run

```bash
python3 train.py run minimum-interval-to-include-each-query
```
