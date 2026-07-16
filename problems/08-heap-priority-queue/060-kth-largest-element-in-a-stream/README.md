# 060. Kth Largest Element In a Stream

- Chapter: 08. Heap / Priority Queue
- Difficulty: Easy
- Source: https://leetcode.com/problems/kth-largest-element-in-a-stream/
- Reference: https://neetcode.io/problems/kth-largest-integer-in-a-stream?list=neetcode150

## Goal

Classic interview problem for Kth Largest Element In a Stream. Practice Top K and two heaps. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: Top K.
- Before coding, state the invariant or state definition: two heaps.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
ops = ['KthLargest', 'add', 'add', 'add', 'add', 'add']
args = [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
expected = [None, 4, 5, 5, 8, 8]
```

### Case 2

```python
ops = ['KthLargest', 'add', 'add', 'add', 'add']
args = [[4, [7, 7, 7, 7, 8, 3]], [2], [10], [9], [9]]
expected = [None, 7, 7, 7, 8]
```

### Case 3

```python
ops = ['KthLargest', 'add', 'add', 'add']
args = [[1, [5]], [2], [3], [1]]
expected = [None, 5, 5, 5]
```

### Case 4

```python
ops = ['KthLargest', 'add']
args = [[1, []], [3]]
expected = [None, 3]
```

### Case 5

```python
ops = ['KthLargest', 'add']
args = [[3, [5, 6]], [7]]
expected = [None, 5]
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run kth-largest-element-in-a-stream
```
