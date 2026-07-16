# 017. Longest Repeating Character Replacement

- Chapter: 03. Sliding Window
- Difficulty: Medium
- Source: https://leetcode.com/problems/longest-repeating-character-replacement/
- Reference: https://neetcode.io/problems/longest-repeating-substring-with-replacement?list=neetcode150

## Goal

Classic interview problem for Longest Repeating Character Replacement. Practice window invariants and left/right boundary movement. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: window invariants.
- Before coding, state the invariant or state definition: left/right boundary movement.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = ['ABAB', 2]
expected = 4
```

### Case 2

```python
args = ['AABABBA', 1]
expected = 4
```

### Case 3

```python
args = ['AAAA', 0]
expected = 4
```

### Case 4

```python
args = ['ABCDE', 0]
expected = 1
```

### Case 5

```python
args = ['ABCDE', 4]
expected = 5
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run longest-repeating-character-replacement
```
