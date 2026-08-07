# 078. Design Add And Search Words Data Structure

- Chapter: 10. Tries
- Difficulty: Medium
- Source: https://leetcode.com/problems/design-add-and-search-words-data-structure/
- Reference: https://neetcode.io/problems/design-word-search-data-structure?list=neetcode150

## Goal

Classic interview problem for Design Add And Search Words Data Structure. Practice trie node design and string search. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: trie node design.
- Before coding, state the invariant or state definition: string search.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

first line q (operations), then q lines of 'op args...'. Output: one result per operation (null for void; space-separated values for lists)

## Local Examples

### Case 1

**Input**

```
8
WordDictionary
addWord bad
addWord dad
addWord mad
search pad
search bad
search .ad
search b..
```

**Output**

```
null
null
null
null
0
1
1
1
```

### Case 2

**Input**

```
5
WordDictionary
addWord a
search a
search .
search aa
```

**Output**

```
null
null
1
1
0
```

### Case 3

**Input**

```
6
WordDictionary
addWord at
addWord and
search an
search .at
search an.
```

**Output**

```
null
null
null
0
0
1
```

## Run

```bash
python3 train.py run design-add-and-search-words-data-structure
```
