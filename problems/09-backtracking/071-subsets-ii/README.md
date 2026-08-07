# 071. Subsets II

- Chapter: 09. Backtracking
- Difficulty: Medium
- Source: https://leetcode.com/problems/subsets-ii/
- Reference: https://neetcode.io/problems/subsets-ii?list=neetcode150

## Goal

Classic interview problem for Subsets II. Practice choice paths and pruning. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: choice paths.
- Before coding, state the invariant or state definition: pruning.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: arg1: an integer list: count n then n integers. Output: each group on its own line (sorted; each group sorted).

## Local Examples

### Case 1

**Input**

```
3
1 2 2
```

**Output**

```

1
1 2
1 2 2
2
2 2
```

### Case 2

**Input**

```
1
0
```

**Output**

```

0
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
python3 train.py run subsets-ii
```
