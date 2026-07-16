# 108. Word Break

- Chapter: 13. 1-D Dynamic Programming
- Difficulty: Medium
- Source: https://leetcode.com/problems/word-break/
- Reference: https://neetcode.io/problems/word-break?list=neetcode150

## Goal

Classic interview problem for Word Break. Practice state definition and transition equations. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: state definition.
- Before coding, state the invariant or state definition: transition equations.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = ['leetcode', ['leet', 'code']]
expected = True
```

### Case 2

```python
args = ['applepenapple', ['apple', 'pen']]
expected = True
```

### Case 3

```python
args = ['catsandog', ['cats', 'dog', 'sand', 'and', 'cat']]
expected = False
```

### Case 4

```python
args = ['', []]
expected = True
```

### Case 5

```python
args = ['a', ['a']]
expected = True
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run word-break
```
