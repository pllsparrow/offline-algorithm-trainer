# 017. Longest Repeating Character Replacement

- Chapter: 03. Sliding Window
- Difficulty: Medium
- Source: https://leetcode.com/problems/longest-repeating-character-replacement/
- Reference: https://neetcode.io/problems/longest-repeating-substring-with-replacement?list=neetcode150

## Goal

Classic interview problem for Longest Repeating Character Replacement. Practice window invariants and left/right boundary movement. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: window invariants.
- Before coding, state the invariant or state definition: left/right boundary movement.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: arg1: a string token; arg2: an integer. Output: the integer.

## Local Examples

### Case 1

**Input**

```
ABAB
2
```

**Output**

```
4
```

### Case 2

**Input**

```
AABABBA
1
```

**Output**

```
4
```

### Case 3

**Input**

```
AAAA
0
```

**Output**

```
4
```

## Run

```bash
python3 train.py run longest-repeating-character-replacement
```
