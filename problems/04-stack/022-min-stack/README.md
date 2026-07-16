# 022. Min Stack

- Chapter: 04. Stack
- Difficulty: Medium
- Source: https://leetcode.com/problems/min-stack/
- Reference: https://neetcode.io/problems/minimum-stack?list=neetcode150

## Goal

Design a stack that can return the minimum value in O(1). Practice maintaining auxiliary stack state.

## Interview Focus

- Identify the core pattern: monotonic stacks.
- Before coding, state the invariant or state definition: parentheses matching.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
ops = ['MinStack', 'push', 'push', 'push', 'getMin', 'pop', 'top', 'getMin']
args = [[], [-2], [0], [-3], [], [], [], []]
expected = [None, None, None, None, -3, None, 0, -2]
```

### Case 2

```python
ops = ['MinStack', 'push', 'top', 'getMin', 'pop']
args = [[], [5], [], [], []]
expected = [None, None, 5, 5, None]
```

### Case 3

```python
ops = ['MinStack', 'push', 'push', 'push', 'getMin', 'pop', 'getMin', 'pop', 'getMin']
args = [[], [1], [1], [2], [], [], [], [], []]
expected = [None, None, None, None, 1, None, 1, None, 1]
```

### Case 4

```python
ops = ['MinStack', 'push', 'getMin', 'top']
args = [[], [0], [], []]
expected = [None, None, 0, 0]
```

### Case 5

```python
ops = ['MinStack', 'push', 'push', 'getMin', 'push', 'getMin', 'pop', 'getMin']
args = [[], [2], [1], [], [0], [], [], []]
expected = [None, None, None, 1, None, 0, None, 1]
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run min-stack
```
