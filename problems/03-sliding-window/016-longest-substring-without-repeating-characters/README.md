# 016. Longest Substring Without Repeating Characters

- Chapter: 03. Sliding Window
- Difficulty: Medium
- Source: https://leetcode.com/problems/longest-substring-without-repeating-characters/
- Reference: https://neetcode.io/problems/longest-substring-without-duplicates?list=neetcode150

## Goal

Classic interview problem for Longest Substring Without Repeating Characters. Practice window invariants and left/right boundary movement. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: window invariants.
- Before coding, state the invariant or state definition: left/right boundary movement.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = ['abcabcbb']
expected = 3
```

### Case 2

```python
args = ['bbbbb']
expected = 1
```

### Case 3

```python
args = ['pwwkew']
expected = 3
```

### Case 4

```python
args = ['']
expected = 0
```

### Case 5

```python
args = ['a']
expected = 1
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run longest-substring-without-repeating-characters
```
