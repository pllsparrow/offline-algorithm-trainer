# 079. Word Search II

- Chapter: 10. Tries
- Difficulty: Hard
- Source: https://leetcode.com/problems/word-search-ii/
- Reference: https://neetcode.io/problems/search-for-word-ii?list=neetcode150

## Goal

Classic interview problem for Word Search II. Practice trie node design and string search. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: trie node design.
- Before coding, state the invariant or state definition: string search.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: arg1: a char board: rows r, cols c, then r lines of c chars; arg2: a string list: count n then n tokens. Output: the values space-separated in ascending order.

## Local Examples

### Case 1

**Input**

```
4 4
o a a n
e t a e
i h k r
i f l v
4
oath
pea
eat
rain
```

**Output**

```
eat oath
```

### Case 2

**Input**

```
2 2
a b
c d
1
abcb
```

**Output**

```
```

### Case 3

**Input**

```
1 1
a
1
a
```

**Output**

```
a
```

## Run

```bash
python3 train.py run word-search-ii
```
