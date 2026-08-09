# 103. Longest Palindromic Substring

- Chapter: 13. 1-D Dynamic Programming
- Difficulty: Medium
- Source: https://leetcode.com/problems/longest-palindromic-substring/
- Reference: https://neetcode.io/problems/longest-palindromic-substring?list=neetcode150

## Goal

Classic interview problem for Longest Palindromic Substring. Practice state definition and transition equations. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: state definition.
- Before coding, state the invariant or state definition: transition equations.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: s: a string token. Output: the strings space-separated.

## Local Examples

### Case 1

**Input**

```
babad
```

**Output**

```
aba bab
```

### Case 2

**Input**

```
cbbd
```

**Output**

```
bb
```

### Case 3

**Input**

```
a
```

**Output**

```
a
```

## Run

```bash
python3 train.py run longest-palindromic-substring
```
