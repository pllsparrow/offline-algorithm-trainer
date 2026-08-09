# 130. Insert Interval

- Chapter: 16. Intervals
- Difficulty: Medium
- Source: https://leetcode.com/problems/insert-interval/
- Reference: https://neetcode.io/problems/insert-new-interval?list=neetcode150

## Goal

Classic interview problem for Insert Interval. Practice sorting then merging and overlap checks. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: sorting then merging.
- Before coding, state the invariant or state definition: overlap checks.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: intervals: edges2: count then values; new_interval: an integer list: count n then n integers. Output: count m then m lines of pairs.

## Local Examples

### Case 1

**Input**

```
2
1 3
6 9
2
2 5
```

**Output**

```
2
1 5
6 9
```

### Case 2

**Input**

```
5
1 2
3 5
6 7
8 10
12 16
2
4 8
```

**Output**

```
3
1 2
3 10
12 16
```

### Case 3

**Input**

```
0
2
5 7
```

**Output**

```
1
5 7
```

## Run

```bash
python3 train.py run insert-interval
```
