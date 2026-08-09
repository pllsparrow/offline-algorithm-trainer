# 121. Regular Expression Matching

- Chapter: 14. 2-D Dynamic Programming
- Difficulty: Hard
- Source: https://leetcode.com/problems/regular-expression-matching/
- Reference: https://neetcode.io/problems/regular-expression-matching?list=neetcode150

## Goal

Classic interview problem for Regular Expression Matching. Practice 2D state design and string DP. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: 2D state design.
- Before coding, state the invariant or state definition: string DP.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: s: a string token; p: a string token. Output: 1 if true else 0.

## Local Examples

### Case 1

**Input**

```
aa
a
```

**Output**

```
0
```

### Case 2

**Input**

```
aa
a*
```

**Output**

```
1
```

### Case 3

**Input**

```
ab
.*
```

**Output**

```
1
```

## Run

```bash
python3 train.py run regular-expression-matching
```
