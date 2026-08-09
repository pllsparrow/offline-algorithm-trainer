# 134. Meeting Rooms II

- Chapter: 16. Intervals
- Difficulty: Medium
- Source: https://leetcode.com/problems/meeting-rooms-ii/
- Reference: https://neetcode.io/problems/meeting-schedule-ii?list=neetcode150

## Goal

Classic interview problem for Meeting Rooms II. Practice sorting then merging and overlap checks. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: sorting then merging.
- Before coding, state the invariant or state definition: overlap checks.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: intervals: edges2: count then values. Output: the integer.

## Local Examples

### Case 1

**Input**

```
3
0 30
5 10
15 20
```

**Output**

```
2
```

### Case 2

**Input**

```
2
7 10
2 4
```

**Output**

```
1
```

### Case 3

**Input**

```
1
1 5
```

**Output**

```
1
```

## Run

```bash
python3 train.py run meeting-rooms-ii
```
