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

## Local Examples

### Case 1

```python
args = [['Hello', 'World']]
expected = ['Hello', 'World']
```

### Case 2

```python
args = [['abc', 'def']]
expected = ['abc', 'def']
```

### Case 3

```python
args = [['']]
expected = ['']
```

### Case 4

```python
args = [['a', 'b', 'c']]
expected = ['a', 'b', 'c']
```

### Case 5

```python
args = [['', '', '']]
expected = ['', '', '']
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run encode-and-decode-strings
```
