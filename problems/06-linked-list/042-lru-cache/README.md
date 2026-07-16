# 042. LRU Cache

- Chapter: 06. Linked List
- Difficulty: Medium
- Source: https://leetcode.com/problems/lru-cache/
- Reference: https://neetcode.io/problems/lru-cache?list=neetcode150

## Goal

Classic interview problem for LRU Cache. Practice pointer rewiring and fast and slow pointers. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: pointer rewiring.
- Before coding, state the invariant or state definition: fast and slow pointers.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
ops = ['LRUCache', 'put', 'put', 'get', 'put', 'get', 'put', 'get', 'get', 'get']
args = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
expected = [None, None, None, 1, None, -1, None, -1, 3, 4]
```

### Case 2

```python
ops = ['LRUCache', 'get', 'put', 'get', 'put', 'put', 'get', 'get']
args = [[2], [2], [2, 6], [1], [1, 5], [1, 2], [1], [2]]
expected = [None, -1, None, -1, None, None, 2, 6]
```

### Case 3

```python
ops = ['LRUCache', 'put', 'get', 'put', 'get', 'get']
args = [[1], [2, 1], [2], [3, 2], [2], [3]]
expected = [None, None, 1, None, -1, 2]
```

### Case 4

```python
ops = ['LRUCache', 'get']
args = [[1], [1]]
expected = [None, -1]
```

### Case 5

```python
ops = ['LRUCache', 'put', 'get']
args = [[1], [1, 100], [1]]
expected = [None, None, 100]
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run lru-cache
```
