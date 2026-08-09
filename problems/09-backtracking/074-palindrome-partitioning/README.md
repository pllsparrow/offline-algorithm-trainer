# 074. Palindrome Partitioning

- Chapter: 09. Backtracking
- Difficulty: Medium
- Source: https://leetcode.com/problems/palindrome-partitioning/
- Reference: https://neetcode.io/problems/palindrome-partitioning?list=neetcode150

## Goal

Classic interview problem for Palindrome Partitioning. Practice choice paths and pruning. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: choice paths.
- Before coding, state the invariant or state definition: pruning.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: s: a string token. Output: each group on its own line (sorted; each group sorted).

## Local Examples

### Case 1

**Input**

```
aab
```

**Output**

```
a a b
aa b
```

### Case 2

**Input**

```
a
```

**Output**

```
a
```

### Case 3

**Input**

```
ab
```

**Output**

```
a b
```

## Run

```bash
python3 train.py run palindrome-partitioning
```
