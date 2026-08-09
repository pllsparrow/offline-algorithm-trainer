# 002. Valid Anagram

- Chapter: 01. Arrays & Hashing
- Difficulty: Easy
- Source: https://leetcode.com/problems/valid-anagram/
- Reference: https://neetcode.io/problems/is-anagram?list=neetcode150

## Goal

Determine whether two strings contain the same characters with the same counts. Practice character frequency counting.

## Interview Focus

- Identify the core pattern: hash table modeling.
- Before coding, state the invariant or state definition: frequency counting.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: s: a string token; t: a string token. Output: 1 if true else 0.

## Local Examples

### Case 1

**Input**

```
anagram
nagaram
```

**Output**

```
1
```

### Case 2

**Input**

```
rat
car
```

**Output**

```
0
```

### Case 3

**Input**

```
listen
silent
```

**Output**

```
1
```

## Run

```bash
python3 train.py run valid-anagram
```
