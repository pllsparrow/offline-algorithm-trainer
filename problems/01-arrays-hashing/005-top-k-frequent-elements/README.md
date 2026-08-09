# 005. Top K Frequent Elements

- Chapter: 01. Arrays & Hashing
- Difficulty: Medium
- Source: https://leetcode.com/problems/top-k-frequent-elements/
- Reference: https://neetcode.io/problems/top-k-elements-in-list?list=neetcode150

## Goal

Return the k most frequent elements. Practice frequency counting, heaps, and bucket-style thinking.

## Interview Focus

- Identify the core pattern: hash table modeling.
- Before coding, state the invariant or state definition: frequency counting.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: nums: an integer list: count n then n integers; k: an integer. Output: the values space-separated in ascending order.

## Local Examples

### Case 1

**Input**

```
6
1 1 1 2 2 3
2
```

**Output**

```
1 2
```

### Case 2

**Input**

```
1
1
1
```

**Output**

```
1
```

### Case 3

**Input**

```
10
1 2 1 2 1 2 3 1 3 2
2
```

**Output**

```
1 2
```

## Run

```bash
python3 train.py run top-k-frequent-elements
```
