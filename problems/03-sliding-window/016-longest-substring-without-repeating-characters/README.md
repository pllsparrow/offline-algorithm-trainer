# 016. Longest Substring Without Repeating Characters

- Chapter: 03. Sliding Window
- Difficulty: Medium
- Source: https://leetcode.com/problems/longest-substring-without-repeating-characters/
- Reference: https://neetcode.io/problems/longest-substring-without-duplicates?list=neetcode150

## Goal

Classic interview problem for Longest Substring Without Repeating Characters. Practice window invariants and left/right boundary movement. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: window invariants.
- Before coding, state the invariant or state definition: left/right boundary movement.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: arg1: a whole input line (may contain spaces). Output: the integer.

## Local Examples

### Case 1

**Input**

```
abcabcbb
```

**Output**

```
3
```

### Case 2

**Input**

```
bbbbb
```

**Output**

```
1
```

### Case 3

**Input**

```
pwwkew
```

**Output**

```
3
```

## Run

```bash
python3 train.py run longest-substring-without-repeating-characters
```
