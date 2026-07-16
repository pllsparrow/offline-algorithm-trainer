# 063. Kth Largest Element In An Array

- Chapter: 08. Heap / Priority Queue
- Difficulty: Medium
- Source: https://leetcode.com/problems/kth-largest-element-in-an-array/
- Reference: https://neetcode.io/problems/kth-largest-element-in-an-array?list=neetcode150

## Goal

Classic interview problem for Kth Largest Element In An Array. Practice Top K and two heaps. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: Top K.
- Before coding, state the invariant or state definition: two heaps.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [[3, 2, 1, 5, 6, 4], 2]
expected = 5
```

### Case 2

```python
args = [[3, 2, 3, 1, 2, 4, 5, 5, 6], 4]
expected = 4
```

### Case 3

```python
args = [[1], 1]
expected = 1
```

### Case 4

```python
args = [[1, 2], 1]
expected = 2
```

### Case 5

```python
args = [[1, 2], 2]
expected = 1
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run kth-largest-element-in-an-array
```
