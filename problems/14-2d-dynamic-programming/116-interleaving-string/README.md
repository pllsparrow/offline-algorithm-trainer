# 116. Interleaving String

- Chapter: 14. 2-D Dynamic Programming
- Difficulty: Medium
- Source: https://leetcode.com/problems/interleaving-string/
- Reference: https://neetcode.io/problems/interleaving-string?list=neetcode150

## Goal

Classic interview problem for Interleaving String. Practice 2D state design and string DP. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: 2D state design.
- Before coding, state the invariant or state definition: string DP.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = ['aabcc', 'dbbca', 'aadbbcbcac']
expected = True
```

### Case 2

```python
args = ['aabcc', 'dbbca', 'aadbbbaccc']
expected = False
```

### Case 3

```python
args = ['', '', '']
expected = True
```

### Case 4

```python
args = ['', '', 'a']
expected = False
```

### Case 5

```python
args = ['a', '', 'a']
expected = True
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run interleaving-string
```
