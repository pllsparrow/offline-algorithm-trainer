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

## Local Examples

### Case 1

```python
ops = ['WordDictionary', 'addWord', 'addWord', 'addWord', 'search', 'search', 'search', 'search']
args = [[], ['bad'], ['dad'], ['mad'], ['pad'], ['bad'], ['.ad'], ['b..']]
expected = [None, None, None, None, False, True, True, True]
```

### Case 2

```python
ops = ['WordDictionary', 'addWord', 'search', 'search', 'search']
args = [[], ['a'], ['a'], ['.'], ['aa']]
expected = [None, None, True, True, False]
```

### Case 3

```python
ops = ['WordDictionary', 'addWord', 'addWord', 'search', 'search', 'search']
args = [[], ['at'], ['and'], ['an'], ['.at'], ['an.']]
expected = [None, None, None, False, False, True]
```

### Case 4

```python
ops = ['WordDictionary', 'addWord', 'addWord', 'search', 'search']
args = [[], ['word'], ['world'], ['word'], ['wor.']]
expected = [None, None, None, True, True]
```

### Case 5

```python
ops = ['WordDictionary', 'addWord', 'search', 'search']
args = [[], ['test'], ['test'], ['t..t']]
expected = [None, None, True, True]
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run design-add-and-search-words-data-structure
```
