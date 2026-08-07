# 131. Merge Intervals

- Chapter: 16. Intervals
- Difficulty: Medium
- Source: https://leetcode.com/problems/merge-intervals/
- Reference: https://neetcode.io/problems/merge-intervals?list=neetcode150

## Goal

Classic interview problem for Merge Intervals. Practice sorting then merging and overlap checks. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: sorting then merging.
- Before coding, state the invariant or state definition: overlap checks.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: arg1: edges2: count then values. Output: count m then m lines of pairs.

## Local Examples

### Case 1

**Input**

```
4
1 3
2 6
8 10
15 18
```

**Output**

```
3
1 6
8 10
15 18
```

### Case 2

**Input**

```
2
1 4
4 5
```

**Output**

```
1
1 5
```

### Case 3

**Input**

```
2
4 7
1 4
```

**Output**

```
1
1 7
```

## Run

```bash
python3 train.py run merge-intervals
```
