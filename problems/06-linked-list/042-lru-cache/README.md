# 042. LRU Cache

- Chapter: 06. Linked List
- Difficulty: Medium
- Source: https://leetcode.com/problems/lru-cache/
- Reference: https://neetcode.io/problems/lru-cache?list=neetcode150

## Goal

Classic interview problem for LRU Cache. Practice pointer rewiring and fast and slow pointers. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: pointer rewiring.
- Before coding, state the invariant or state definition: fast and slow pointers.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

first line q (operations), then q lines of 'op args...'. Output: one result per operation (null for void; space-separated values for lists)

## Local Examples

### Case 1

**Input**

```
10
LRUCache 2
put 1 1
put 2 2
get 1
put 3 3
get 2
put 4 4
get 1
get 3
get 4
```

**Output**

```
null
null
null
1
null
-1
null
-1
3
4
```

### Case 2

**Input**

```
8
LRUCache 2
get 2
put 2 6
get 1
put 1 5
put 1 2
get 1
get 2
```

**Output**

```
null
-1
null
-1
null
null
2
6
```

### Case 3

**Input**

```
6
LRUCache 1
put 2 1
get 2
put 3 2
get 2
get 3
```

**Output**

```
null
null
1
null
-1
2
```

## Run

```bash
python3 train.py run lru-cache
```
