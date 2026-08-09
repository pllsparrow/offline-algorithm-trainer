# 061. Last Stone Weight

- Chapter: 08. Heap / Priority Queue
- Difficulty: Easy
- Source: https://leetcode.com/problems/last-stone-weight/
- Reference: https://neetcode.io/problems/last-stone-weight?list=neetcode150

## Goal

Classic interview problem for Last Stone Weight. Practice Top K and two heaps. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: Top K.
- Before coding, state the invariant or state definition: two heaps.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: stones: an integer list: count n then n integers. Output: the integer.

## Local Examples

### Case 1

**Input**

```
6
2 7 4 1 8 1
```

**Output**

```
1
```

### Case 2

**Input**

```
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
2
2 2
```

**Output**

```
0
```

## Run

```bash
python3 train.py run last-stone-weight
```
