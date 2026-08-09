# 092. Word Ladder

- Chapter: 11. Graphs
- Difficulty: Hard
- Source: https://leetcode.com/problems/word-ladder/
- Reference: https://neetcode.io/problems/word-ladder?list=neetcode150

## Goal

Classic interview problem for Word Ladder. Practice DFS/BFS and topological sorting. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: DFS/BFS.
- Before coding, state the invariant or state definition: topological sorting.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: begin_word: a string token; end_word: a string token; word_list: a string list: count n then n tokens. Output: the integer.

## Local Examples

### Case 1

**Input**

```
hit
cog
6
hot
dot
dog
lot
log
cog
```

**Output**

```
5
```

### Case 2

**Input**

```
hit
cog
5
hot
dot
dog
lot
log
```

**Output**

```
0
```

### Case 3

**Input**

```
a
c
3
a
b
c
```

**Output**

```
2
```

## Run

```bash
python3 train.py run word-ladder
```
