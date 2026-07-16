# 019. Minimum Window Substring

- Chapter: 03. Sliding Window
- Difficulty: Hard
- Source: https://leetcode.com/problems/minimum-window-substring/
- Reference: https://neetcode.io/problems/minimum-window-with-characters?list=neetcode150

## Goal

Classic interview problem for Minimum Window Substring. Practice window invariants and left/right boundary movement. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: window invariants.
- Before coding, state the invariant or state definition: left/right boundary movement.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = ['ADOBECODEBANC', 'ABC']
expected = 'BANC'
```

### Case 2

```python
args = ['a', 'a']
expected = 'a'
```

### Case 3

```python
args = ['a', 'aa']
expected = ''
```

### Case 4

```python
args = ['ab', 'b']
expected = 'b'
```

### Case 5

```python
args = ['abc', 'cba']
expected = 'abc'
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run minimum-window-substring
```
