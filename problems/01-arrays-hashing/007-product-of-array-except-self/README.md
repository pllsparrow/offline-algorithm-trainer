# 007. Product of Array Except Self

- Chapter: 01. Arrays & Hashing
- Difficulty: Medium
- Source: https://leetcode.com/problems/product-of-array-except-self/
- Reference: https://neetcode.io/problems/products-of-array-discluding-self?list=neetcode150

## Goal

Classic interview problem for Product of Array Except Self. Practice hash table modeling and frequency counting. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: hash table modeling.
- Before coding, state the invariant or state definition: frequency counting.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: arg1: an integer list: count n then n integers. Output: the values space-separated.

## Local Examples

### Case 1

**Input**

```
4
1 2 3 4
```

**Output**

```
24 12 8 6
```

### Case 2

**Input**

```
5
-1 1 0 -3 3
```

**Output**

```
0 0 9 0 0
```

### Case 3

**Input**

```
4
2 3 4 5
```

**Output**

```
60 40 30 24
```

## Run

```bash
python3 train.py run product-of-array-except-self
```
