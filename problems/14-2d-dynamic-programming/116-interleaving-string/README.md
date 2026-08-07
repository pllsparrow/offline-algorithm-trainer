# 116. Interleaving String

- Chapter: 14. 2-D Dynamic Programming
- Difficulty: Medium
- Source: https://leetcode.com/problems/interleaving-string/
- Reference: https://neetcode.io/problems/interleaving-string?list=neetcode150

## Goal

Classic interview problem for Interleaving String. Practice 2D state design and string DP. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: 2D state design.
- Before coding, state the invariant or state definition: string DP.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: arg1: a string token; arg2: a string token; arg3: a string token. Output: 1 if true else 0.

## Local Examples

### Case 1

**Input**

```
aabcc
dbbca
aadbbcbcac
```

**Output**

```
1
```

### Case 2

**Input**

```
aabcc
dbbca
aadbbbaccc
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
python3 train.py run interleaving-string
```
