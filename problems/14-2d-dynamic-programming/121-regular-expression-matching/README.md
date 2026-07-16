# 121. Regular Expression Matching

- Chapter: 14. 2-D Dynamic Programming
- Difficulty: Hard
- Source: https://leetcode.com/problems/regular-expression-matching/
- Reference: https://neetcode.io/problems/regular-expression-matching?list=neetcode150

## Goal

Classic interview problem for Regular Expression Matching. Practice 2D state design and string DP. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: 2D state design.
- Before coding, state the invariant or state definition: string DP.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = ['aa', 'a']
expected = False
```

### Case 2

```python
args = ['aa', 'a*']
expected = True
```

### Case 3

```python
args = ['ab', '.*']
expected = True
```

### Case 4

```python
args = ['aab', 'c*a*b']
expected = True
```

### Case 5

```python
args = ['mississippi', 'mis*is*p*.']
expected = False
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run regular-expression-matching
```
