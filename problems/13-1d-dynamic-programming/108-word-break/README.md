# 108. Word Break

- Chapter: 13. 1-D Dynamic Programming
- Difficulty: Medium
- Source: https://leetcode.com/problems/word-break/
- Reference: https://neetcode.io/problems/word-break?list=neetcode150

## Goal

Classic interview problem for Word Break. Practice state definition and transition equations. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: state definition.
- Before coding, state the invariant or state definition: transition equations.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: arg1: a string token; arg2: a string list: count n then n tokens. Output: 1 if true else 0.

## Local Examples

### Case 1

**Input**

```
leetcode
2
leet
code
```

**Output**

```
1
```

### Case 2

**Input**

```
applepenapple
2
apple
pen
```

**Output**

```
1
```

### Case 3

**Input**

```
catsandog
5
cats
dog
sand
and
cat
```

**Output**

```
0
```

## Run

```bash
python3 train.py run word-break
```
