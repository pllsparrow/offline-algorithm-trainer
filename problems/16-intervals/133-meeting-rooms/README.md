# 133. Meeting Rooms

- Chapter: 16. Intervals
- Difficulty: Easy
- Source: https://leetcode.com/problems/meeting-rooms/
- Reference: https://neetcode.io/problems/meeting-schedule?list=neetcode150

## Goal

Classic interview problem for Meeting Rooms. Practice sorting then merging and overlap checks. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: sorting then merging.
- Before coding, state the invariant or state definition: overlap checks.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: arg1: edges2: count then values. Output: 1 if true else 0.

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
0
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
0
```

**Output**

```
1
```

## Run

```bash
python3 train.py run meeting-rooms
```
