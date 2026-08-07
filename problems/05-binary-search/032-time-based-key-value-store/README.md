# 032. Time Based Key Value Store

- Chapter: 05. Binary Search
- Difficulty: Medium
- Source: https://leetcode.com/problems/time-based-key-value-store/
- Reference: https://neetcode.io/problems/time-based-key-value-store?list=neetcode150

## Goal

Classic interview problem for Time Based Key Value Store. Practice search space definition and boundary shrinking. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: search space definition.
- Before coding, state the invariant or state definition: boundary shrinking.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

first line q (operations), then q lines of 'op args...'. Output: one result per operation (null for void; space-separated values for lists)

## Local Examples

### Case 1

**Input**

```
7
TimeMap
set foo bar 1
get foo 1
get foo 3
set foo bar2 4
get foo 4
get foo 5
```

**Output**

```
null
null
bar
bar
null
bar2
bar2
```

### Case 2

**Input**

```
2
TimeMap
get key 1
```

**Output**

```
null

```

### Case 3

**Input**

```
3
TimeMap
set a val 1
get a 1
```

**Output**

```
null
null
val
```

## Run

```bash
python3 train.py run time-based-key-value-store
```
