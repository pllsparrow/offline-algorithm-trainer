# 076. N Queens

- Chapter: 09. Backtracking
- Difficulty: Hard
- Source: https://leetcode.com/problems/n-queens/
- Reference: https://neetcode.io/problems/n-queens?list=neetcode150

## Goal

Classic interview problem for N Queens. Practice choice paths and pruning. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: choice paths.
- Before coding, state the invariant or state definition: pruning.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: arg1: an integer. Output: the solution count S, then S boards each as n lines of Q/..

## Local Examples

### Case 1

**Input**

```
1
```

**Output**

```
1
Q
```

### Case 2

**Input**

```
2
```

**Output**

```
0
```

### Case 3

**Input**

```
3
```

**Output**

```
0
```

## Run

```bash
python3 train.py run n-queens
```
