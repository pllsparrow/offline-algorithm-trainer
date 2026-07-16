# 066. Find Median From Data Stream

- Chapter: 08. Heap / Priority Queue
- Difficulty: Hard
- Source: https://leetcode.com/problems/find-median-from-data-stream/
- Reference: https://neetcode.io/problems/find-median-in-a-data-stream?list=neetcode150

## Goal

Classic interview problem for Find Median From Data Stream. Practice Top K and two heaps. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: Top K.
- Before coding, state the invariant or state definition: two heaps.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
ops = ['MedianFinder', 'addNum', 'addNum', 'findMedian', 'addNum', 'findMedian']
args = [[], [1], [2], [], [3], []]
expected = [None, None, None, 1.5, None, 2.0]
```

### Case 2

```python
ops = ['MedianFinder', 'addNum', 'findMedian']
args = [[], [1], []]
expected = [None, None, 1.0]
```

### Case 3

```python
ops = ['MedianFinder', 'addNum', 'addNum', 'addNum', 'findMedian']
args = [[], [1], [1], [1], []]
expected = [None, None, None, None, 1.0]
```

### Case 4

```python
ops = ['MedianFinder', 'addNum', 'addNum', 'addNum', 'addNum', 'findMedian']
args = [[], [1], [2], [3], [4], []]
expected = [None, None, None, None, None, 2.5]
```

### Case 5

```python
ops = ['MedianFinder', 'addNum', 'addNum', 'findMedian', 'addNum', 'addNum', 'findMedian']
args = [[], [-1], [0], [], [1], [2], []]
expected = [None, None, None, -0.5, None, None, 0.5]
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run find-median-from-data-stream
```
