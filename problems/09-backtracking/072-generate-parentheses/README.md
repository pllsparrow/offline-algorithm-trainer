# 072. Generate Parentheses

- Chapter: 09. Backtracking
- Difficulty: Medium
- Source: https://leetcode.com/problems/generate-parentheses/
- Reference: https://neetcode.io/problems/generate-parentheses?list=neetcode150

## Goal

Classic interview problem for Generate Parentheses. Practice choice paths and pruning. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: choice paths.
- Before coding, state the invariant or state definition: pruning.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: n: an integer. Output: the values space-separated in ascending order.

## Local Examples

### Case 1

**Input**

```
1
```

**Output**

```
()
```

### Case 2

**Input**

```
2
```

**Output**

```
(()) ()()
```

### Case 3

**Input**

```
3
```

**Output**

```
((())) (()()) (())() ()(()) ()()()
```

## Run

```bash
python3 train.py run generate-parentheses
```
