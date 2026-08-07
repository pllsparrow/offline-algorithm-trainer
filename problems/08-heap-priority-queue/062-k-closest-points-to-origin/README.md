# 062. K Closest Points to Origin

- Chapter: 08. Heap / Priority Queue
- Difficulty: Medium
- Source: https://leetcode.com/problems/k-closest-points-to-origin/
- Reference: https://neetcode.io/problems/k-closest-points-to-origin?list=neetcode150

## Goal

Classic interview problem for K Closest Points to Origin. Practice Top K and two heaps. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: Top K.
- Before coding, state the invariant or state definition: two heaps.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: arg1: edges2: count then values; arg2: an integer. Output: each group on its own line (sorted; each group sorted).

## Local Examples

### Case 1

**Input**

```
2
1 3
-2 2
1
```

**Output**

```
-2 2
```

### Case 2

**Input**

```
3
3 3
5 -1
-2 4
2
```

**Output**

```
-2 4
3 3
```

### Case 3

**Input**

```
2
0 1
1 0
2
```

**Output**

```
0 1
0 1
```

## Run

```bash
python3 train.py run k-closest-points-to-origin
```
