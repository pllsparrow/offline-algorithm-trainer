# 077. Implement Trie Prefix Tree

- Chapter: 10. Tries
- Difficulty: Medium
- Source: https://leetcode.com/problems/implement-trie-prefix-tree/
- Reference: https://neetcode.io/problems/implement-prefix-tree?list=neetcode150

## Goal

Classic interview problem for Implement Trie Prefix Tree. Practice trie node design and string search. Start with a brute-force idea, then optimize to an interview-ready complexity.

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
6
Trie
insert app
insert apple
search app
search apple
search appl
```

**Output**

```
null
null
null
1
1
0
```

### Case 2

**Input**

```
7
Trie
insert cat
insert car
insert card
search cat
search car
search care
```

**Output**

```
null
null
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
Trie
insert test
insert testing
starts_with test
starts_with testing
starts_with te
```

**Output**

```
null
null
null
1
1
1
```

## Run

```bash
python3 train.py run implement-trie-prefix-tree
```
