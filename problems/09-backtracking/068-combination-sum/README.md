# 068. Combination Sum

- Chapter: 09. Backtracking
- Difficulty: Medium
- Source: https://leetcode.com/problems/combination-sum/
- Reference: https://neetcode.io/problems/combination-target-sum?list=neetcode150

## Goal

Classic interview problem for Combination Sum. Practice choice paths and pruning. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: choice paths.
- Before coding, state the invariant or state definition: pruning.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: candidates: an integer list: count n then n integers; target: an integer. Output: each group on its own line (sorted; each group sorted).

## Local Examples

### Case 1

**Input**

```
4
2 3 6 7
7
```

**Output**

```
2 2 3
7
```

### Case 2

**Input**

```
3
2 3 5
8
```

**Output**

```
2 2 2 2
2 3 3
3 5
```

### Case 3

**Input**

```
1
2
1
```

**Output**

```
```

## Run

```bash
python3 train.py run combination-sum
```
