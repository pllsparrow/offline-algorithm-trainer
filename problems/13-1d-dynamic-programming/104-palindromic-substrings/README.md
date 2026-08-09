# 104. Palindromic Substrings

- Chapter: 13. 1-D Dynamic Programming
- Difficulty: Medium
- Source: https://leetcode.com/problems/palindromic-substrings/
- Reference: https://neetcode.io/problems/palindromic-substrings?list=neetcode150

## Goal

Classic interview problem for Palindromic Substrings. Practice state definition and transition equations. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: state definition.
- Before coding, state the invariant or state definition: transition equations.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: s: a string token. Output: the integer.

## Local Examples

### Case 1

**Input**

```
abc
```

**Output**

```
3
```

### Case 2

**Input**

```
aaa
```

**Output**

```
6
```

### Case 3

**Input**

```
a
```

**Output**

```
1
```

## Run

```bash
python3 train.py run palindromic-substrings
```
