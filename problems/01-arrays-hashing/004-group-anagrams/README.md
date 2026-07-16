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

## Local Examples

### Case 1

```python
args = [['eat', 'tea', 'tan', 'ate', 'nat', 'bat']]
expected = [['bat'], ['nat', 'tan'], ['ate', 'eat', 'tea']]
```

### Case 2

```python
args = [['']]
expected = [['']]
```

### Case 3

```python
args = [['a']]
expected = [['a']]
```

### Case 4

```python
args = [['abc', 'bca', 'cab', 'xyz']]
expected = [['abc', 'bca', 'cab'], ['xyz']]
```

### Case 5

```python
args = [['ab', 'ba']]
expected = [['ab', 'ba']]
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run group-anagrams
```
