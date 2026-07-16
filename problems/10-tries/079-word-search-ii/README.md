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

## Local Examples

### Case 1

```python
args = [[['o', 'a', 'a', 'n'], ['e', 't', 'a', 'e'], ['i', 'h', 'k', 'r'], ['i', 'f', 'l', 'v']], ['oath', 'pea', 'eat', 'rain']]
expected = ['eat', 'oath']
```

### Case 2

```python
args = [[['a', 'b'], ['c', 'd']], ['abcb']]
expected = []
```

### Case 3

```python
args = [[['a']], ['a']]
expected = ['a']
```

### Case 4

```python
args = [[['a']], ['b']]
expected = []
```

### Case 5

```python
args = [[['a', 'a'], ['a', 'a']], ['aaaa']]
expected = ['aaaa']
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run word-search-ii
```
