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

## Local Examples

### Case 1

```python
ops = ['Trie', 'insert', 'insert', 'search', 'search', 'search']
args = [[], ['app'], ['apple'], ['app'], ['apple'], ['appl']]
expected = [None, None, None, True, True, False]
```

### Case 2

```python
ops = ['Trie', 'insert', 'insert', 'insert', 'search', 'search', 'search']
args = [[], ['cat'], ['car'], ['card'], ['cat'], ['car'], ['care']]
expected = [None, None, None, None, True, True, False]
```

### Case 3

```python
ops = ['Trie', 'insert', 'insert', 'starts_with', 'starts_with', 'starts_with']
args = [[], ['test'], ['testing'], ['test'], ['testing'], ['te']]
expected = [None, None, None, True, True, True]
```

### Case 4

```python
ops = ['Trie', 'insert', 'search', 'search', 'insert', 'search', 'search']
args = [[], ['abc'], ['abc'], ['ab'], ['ab'], ['ab'], ['abc']]
expected = [None, None, True, False, None, True, True]
```

### Case 5

```python
ops = ['Trie', 'insert', 'search', 'starts_with']
args = [[], ['a'], ['a'], ['a']]
expected = [None, None, True, True]
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run implement-trie-prefix-tree
```
