# 069. Combination Sum II

- Chapter: 09. Backtracking
- Difficulty: Medium
- Source: https://leetcode.com/problems/combination-sum-ii/
- Reference: https://neetcode.io/problems/combination-target-sum-ii?list=neetcode150

## Goal

Classic interview problem for Combination Sum II. Practice choice paths and pruning. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: choice paths.
- Before coding, state the invariant or state definition: pruning.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: arg1: an integer list: count n then n integers; arg2: an integer. Output: each group on its own line (sorted; each group sorted).

## Local Examples

### Case 1

**Input**

```
7
10 1 2 7 6 1 5
8
```

**Output**

```
1 1 6
1 2 5
1 7
2 6
```

### Case 2

**Input**

```
5
2 5 2 1 2
5
```

**Output**

```
1 2 2
5
```

### Case 3

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

## Run

```bash
python3 train.py run combination-sum-ii
```
