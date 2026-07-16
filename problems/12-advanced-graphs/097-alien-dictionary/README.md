# 097. Alien Dictionary

- Chapter: 12. Advanced Graphs
- Difficulty: Hard
- Source: https://leetcode.com/problems/alien-dictionary/
- Reference: https://neetcode.io/problems/foreign-dictionary?list=neetcode150

## Goal

Classic interview problem for Alien Dictionary. Practice shortest paths and minimum spanning trees. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: shortest paths.
- Before coding, state the invariant or state definition: minimum spanning trees.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [['wrt', 'wrf', 'er', 'ett', 'rftt']]
expected = 'wertf'
```

### Case 2

```python
args = [['z', 'x']]
expected = 'zx'
```

### Case 3

```python
args = [['z', 'x', 'z']]
expected = ''
```

### Case 4

```python
args = [['z', 'z']]
expected = 'z'
```

### Case 5

```python
args = [['abc', 'ab']]
expected = ''
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run alien-dictionary
```
