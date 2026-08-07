# 018. Permutation In String

- Chapter: 03. Sliding Window
- Difficulty: Medium
- Source: https://leetcode.com/problems/permutation-in-string/
- Reference: https://neetcode.io/problems/permutation-string?list=neetcode150

## Goal

Classic interview problem for Permutation In String. Practice window invariants and left/right boundary movement. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: window invariants.
- Before coding, state the invariant or state definition: left/right boundary movement.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: arg1: a string token; arg2: a string token. Output: 1 if true else 0.

## Local Examples

### Case 1

**Input**

```
ab
eidbaooo
```

**Output**

```
1
```

### Case 2

**Input**

```
ab
eidboaoo
```

**Output**

```
0
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
python3 train.py run permutation-in-string
```
