# 097. Alien Dictionary

- Chapter: 12. Advanced Graphs
- Difficulty: Hard
- Source: https://leetcode.com/problems/alien-dictionary/
- Reference: https://neetcode.io/problems/foreign-dictionary?list=neetcode150

## Goal

Classic interview problem for Alien Dictionary. Practice shortest paths and minimum spanning trees. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: shortest paths.
- Before coding, state the invariant or state definition: minimum spanning trees.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: words: a string list: count n then n tokens. Output: the string.

## Local Examples

### Case 1

**Input**

```
5
wrt
wrf
er
ett
rftt
```

**Output**

```
wertf
```

### Case 2

**Input**

```
2
z
x
```

**Output**

```
zx
```

### Case 3

**Input**

```
3
z
x
z
```

**Output**

```

```

## Run

```bash
python3 train.py run alien-dictionary
```
