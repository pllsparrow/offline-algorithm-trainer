# 019. Minimum Window Substring

- Chapter: 03. Sliding Window
- Difficulty: Hard
- Source: https://leetcode.com/problems/minimum-window-substring/
- Reference: https://neetcode.io/problems/minimum-window-with-characters?list=neetcode150

## Goal

Classic interview problem for Minimum Window Substring. Practice window invariants and left/right boundary movement. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: window invariants.
- Before coding, state the invariant or state definition: left/right boundary movement.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: s: a string token; t: a string token. Output: the string.

## Local Examples

### Case 1

**Input**

```
ADOBECODEBANC
ABC
```

**Output**

```
BANC
```

### Case 2

**Input**

```
a
a
```

**Output**

```
a
```

### Case 3

**Input**

```
a
aa
```

**Output**

```

```

## Run

```bash
python3 train.py run minimum-window-substring
```
