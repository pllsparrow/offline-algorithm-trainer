# 018. Permutation In String

- Chapter: 03. Sliding Window
- Difficulty: Medium
- Source: https://leetcode.com/problems/permutation-in-string/
- Reference: https://neetcode.io/problems/permutation-string?list=neetcode150

## Goal

Classic interview problem for Permutation In String. Practice window invariants and left/right boundary movement. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: window invariants.
- Before coding, state the invariant or state definition: left/right boundary movement.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = ['ab', 'eidbaooo']
expected = True
```

### Case 2

```python
args = ['ab', 'eidboaoo']
expected = False
```

### Case 3

```python
args = ['a', 'a']
expected = True
```

### Case 4

```python
args = ['ab', 'ab']
expected = True
```

### Case 5

```python
args = ['abc', 'bbbca']
expected = True
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run permutation-in-string
```
