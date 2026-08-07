# 112. Longest Common Subsequence

- Chapter: 14. 2-D Dynamic Programming
- Difficulty: Medium
- Source: https://leetcode.com/problems/longest-common-subsequence/
- Reference: https://neetcode.io/problems/longest-common-subsequence?list=neetcode150

## Goal

Classic interview problem for Longest Common Subsequence. Practice 2D state design and string DP. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: 2D state design.
- Before coding, state the invariant or state definition: string DP.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: arg1: a string token; arg2: a string token. Output: the integer.

## Local Examples

### Case 1

**Input**

```
abcde
ace
```

**Output**

```
3
```

### Case 2

**Input**

```
abc
abc
```

**Output**

```
3
```

### Case 3

**Input**

```
abc
def
```

**Output**

```
0
```

## Run

```bash
python3 train.py run longest-common-subsequence
```
