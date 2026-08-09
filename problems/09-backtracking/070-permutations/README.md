# 070. Permutations

- Chapter: 09. Backtracking
- Difficulty: Medium
- Source: https://leetcode.com/problems/permutations/
- Reference: https://neetcode.io/problems/permutations?list=neetcode150

## Goal

Classic interview problem for Permutations. Practice choice paths and pruning. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: choice paths.
- Before coding, state the invariant or state definition: pruning.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: nums: an integer list: count n then n integers. Output: each group on its own line (sorted; each group sorted).

## Local Examples

### Case 1

**Input**

```
3
1 2 3
```

**Output**

```
1 2 3
1 2 3
1 2 3
1 2 3
1 2 3
1 2 3
```

### Case 2

**Input**

```
2
0 1
```

**Output**

```
0 1
0 1
```

### Case 3

**Input**

```
1
1
```

**Output**

```
1
```

## Run

```bash
python3 train.py run permutations
```
