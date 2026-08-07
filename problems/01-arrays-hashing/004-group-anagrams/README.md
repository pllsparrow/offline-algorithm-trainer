# 004. Group Anagrams

- Chapter: 01. Arrays & Hashing
- Difficulty: Medium
- Source: https://leetcode.com/problems/group-anagrams/
- Reference: https://neetcode.io/problems/anagram-groups?list=neetcode150

## Goal

Group strings that are anagrams of each other. Practice turning a complex object into a stable grouping key.

## Interview Focus

- Identify the core pattern: hash table modeling.
- Before coding, state the invariant or state definition: frequency counting.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: arg1: a string list: count n then n tokens. Output: each group on its own line (sorted; each group sorted).

## Local Examples

### Case 1

**Input**

```
6
eat
tea
tan
ate
nat
bat
```

**Output**

```
ate eat tea
bat
nat tan
```

### Case 2

**Input**

```
1

```

**Output**

```

```

### Case 3

**Input**

```
1
a
```

**Output**

```
a
```

## Run

```bash
python3 train.py run group-anagrams
```
