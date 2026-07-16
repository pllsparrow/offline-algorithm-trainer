# 005. Top K Frequent Elements

- Chapter: 01. Arrays & Hashing
- Difficulty: Medium
- Source: https://leetcode.com/problems/top-k-frequent-elements/
- Reference: https://neetcode.io/problems/top-k-elements-in-list?list=neetcode150

## Goal

Return the k most frequent elements. Practice frequency counting, heaps, and bucket-style thinking.

## Interview Focus

- Identify the core pattern: hash table modeling.
- Before coding, state the invariant or state definition: frequency counting.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [[1, 1, 1, 2, 2, 3], 2]
expected = [1, 2]
```

### Case 2

```python
args = [[1], 1]
expected = [1]
```

### Case 3

```python
args = [[1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2]
expected = [1, 2]
```

### Case 4

```python
args = [[1, 2, 3, 4, 5], 1]
expected = [1]
```

### Case 5

```python
args = [[1, 1, 2, 2, 3, 3], 3]
expected = [1, 2, 3]
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run top-k-frequent-elements
```
