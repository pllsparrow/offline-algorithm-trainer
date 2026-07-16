# 032. Time Based Key Value Store

- Chapter: 05. Binary Search
- Difficulty: Medium
- Source: https://leetcode.com/problems/time-based-key-value-store/
- Reference: https://neetcode.io/problems/time-based-key-value-store?list=neetcode150

## Goal

Classic interview problem for Time Based Key Value Store. Practice search space definition and boundary shrinking. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: search space definition.
- Before coding, state the invariant or state definition: boundary shrinking.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
ops = ['TimeMap', 'set', 'get', 'get', 'set', 'get', 'get']
args = [[], ['foo', 'bar', 1], ['foo', 1], ['foo', 3], ['foo', 'bar2', 4], ['foo', 4], ['foo', 5]]
expected = [None, None, 'bar', 'bar', None, 'bar2', 'bar2']
```

### Case 2

```python
ops = ['TimeMap', 'get']
args = [[], ['key', 1]]
expected = [None, '']
```

### Case 3

```python
ops = ['TimeMap', 'set', 'get']
args = [[], ['a', 'val', 1], ['a', 1]]
expected = [None, None, 'val']
```

### Case 4

```python
ops = ['TimeMap', 'set', 'get', 'get']
args = [[], ['key', 'value', 5], ['key', 3], ['key', 7]]
expected = [None, None, '', 'value']
```

### Case 5

```python
ops = ['TimeMap', 'set', 'set', 'get', 'get', 'get']
args = [[], ['x', 'v1', 1], ['x', 'v2', 2], ['x', 1], ['x', 2], ['x', 3]]
expected = [None, None, None, 'v1', 'v2', 'v2']
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run time-based-key-value-store
```
