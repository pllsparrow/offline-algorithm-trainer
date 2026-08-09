# 006. Encode and Decode Strings

- Chapter: 01. Arrays & Hashing
- Difficulty: Medium
- Source: https://leetcode.com/problems/encode-and-decode-strings/
- Reference: https://neetcode.io/problems/string-encode-and-decode?list=neetcode150

## Goal

Classic interview problem for Encode and Decode Strings. Practice hash table modeling and frequency counting. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: hash table modeling.
- Before coding, state the invariant or state definition: frequency counting.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: strs: strings with length prefix: count n, then per string a length line and the raw bytes. Output: count n, then per string a length line and the raw bytes (round-trip of the input).

## Local Examples

### Case 1

**Input**

```
2
5
Hello
5
World
```

**Output**

```
2
5
Hello
5
World
```

### Case 2

**Input**

```
2
3
abc
3
def
```

**Output**

```
2
3
abc
3
def
```

### Case 3

**Input**

```
1
0

```

**Output**

```
1
0

```

## Run

```bash
python3 train.py run encode-and-decode-strings
```
