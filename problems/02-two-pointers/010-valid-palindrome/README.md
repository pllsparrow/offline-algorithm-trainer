# 010. Valid Palindrome

- Chapter: 02. Two Pointers
- Difficulty: Easy
- Source: https://leetcode.com/problems/valid-palindrome/
- Reference: https://neetcode.io/problems/is-palindrome?list=neetcode150

## Goal

Check whether a string is a palindrome after ignoring case and non-alphanumeric characters. Practice two-pointer scanning.

## Interview Focus

- Identify the core pattern: left/right pointers.
- Before coding, state the invariant or state definition: sorted array scanning.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: arg1: a whole input line (may contain spaces). Output: 1 if true else 0.

## Local Examples

### Case 1

**Input**

```
A man, a plan, a canal: Panama
```

**Output**

```
1
```

### Case 2

**Input**

```
race a car
```

**Output**

```
0
```

### Case 3

**Input**

```
 
```

**Output**

```
1
```

## Run

```bash
python3 train.py run valid-palindrome
```
