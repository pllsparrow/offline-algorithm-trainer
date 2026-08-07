# 003. Two Sum

- Chapter: 01. Arrays & Hashing
- Difficulty: Easy
- Source: https://leetcode.com/problems/two-sum/
- Reference: https://neetcode.io/problems/two-integer-sum?list=neetcode150

## Goal

Find the indices of two numbers whose sum equals the target. Practice looking up complements while traversing with a hash table.

## Interview Focus

- Identify the core pattern: hash table modeling.
- Before coding, state the invariant or state definition: frequency counting.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: arg1: an integer list: count n then n integers; arg2: an integer. Output: the values space-separated.

## Local Examples

### Case 1

**Input**

```
4
2 7 11 15
9
```

**Output**

```
0 1
```

### Case 2

**Input**

```
3
3 2 4
6
```

**Output**

```
1 2
```

### Case 3

**Input**

```
2
3 3
6
```

**Output**

```
0 1
```

## Run

```bash
python3 train.py run two-sum
```
