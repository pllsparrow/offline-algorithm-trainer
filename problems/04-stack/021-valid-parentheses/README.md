# 021. Valid Parentheses

- Chapter: 04. Stack
- Difficulty: Easy
- Source: https://leetcode.com/problems/valid-parentheses/
- Reference: https://neetcode.io/problems/validate-parentheses?list=neetcode150

## Goal

Classic interview problem for Valid Parentheses. Practice monotonic stacks and parentheses matching. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: monotonic stacks.
- Before coding, state the invariant or state definition: parentheses matching.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: s: a string token. Output: 1 if true else 0.

## Local Examples

### Case 1

**Input**

```
()
```

**Output**

```
1
```

### Case 2

**Input**

```
()[]{}
```

**Output**

```
1
```

### Case 3

**Input**

```
(]
```

**Output**

```
0
```

## Run

```bash
python3 train.py run valid-parentheses
```
