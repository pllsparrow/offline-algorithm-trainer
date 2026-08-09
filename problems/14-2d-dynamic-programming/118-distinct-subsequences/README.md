# 118. Distinct Subsequences

- Chapter: 14. 2-D Dynamic Programming
- Difficulty: Hard
- Source: https://leetcode.com/problems/distinct-subsequences/
- Reference: https://neetcode.io/problems/count-subsequences?list=neetcode150

## Goal

Classic interview problem for Distinct Subsequences. Practice 2D state design and string DP. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: 2D state design.
- Before coding, state the invariant or state definition: string DP.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: s: a string token; t: a string token. Output: the integer.

## Local Examples

### Case 1

**Input**

```
rabbbit
rabbit
```

**Output**

```
3
```

### Case 2

**Input**

```
babgbag
bag
```

**Output**

```
5
```

### Case 3

**Input**

```
a
a
```

**Output**

```
1
```

## Run

```bash
python3 train.py run distinct-subsequences
```
