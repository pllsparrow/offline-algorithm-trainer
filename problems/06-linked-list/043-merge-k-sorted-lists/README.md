# 043. Merge K Sorted Lists

- Chapter: 06. Linked List
- Difficulty: Hard
- Source: https://leetcode.com/problems/merge-k-sorted-lists/
- Reference: https://neetcode.io/problems/merge-k-sorted-linked-lists?list=neetcode150

## Goal

Classic interview problem for Merge K Sorted Lists. Practice pointer rewiring and fast and slow pointers. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: pointer rewiring.
- Before coding, state the invariant or state definition: fast and slow pointers.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [[[1, 4, 5], [1, 3, 4], [2, 6]]]
expected = [1, 1, 2, 3, 4, 4, 5, 6]
```

### Case 2

```python
args = [[]]
expected = []
```

### Case 3

```python
args = [[[]]]
expected = []
```

### Case 4

```python
args = [[[1]]]
expected = [1]
```

### Case 5

```python
args = [[[1, 2], [3, 4]]]
expected = [1, 2, 3, 4]
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run merge-k-sorted-lists
```
