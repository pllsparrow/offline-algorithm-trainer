# 038. Remove Nth Node From End of List

- Chapter: 06. Linked List
- Difficulty: Medium
- Source: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
- Reference: https://neetcode.io/problems/remove-node-from-end-of-linked-list?list=neetcode150

## Goal

Classic interview problem for Remove Nth Node From End of List. Practice pointer rewiring and fast and slow pointers. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: pointer rewiring.
- Before coding, state the invariant or state definition: fast and slow pointers.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [[1, 2, 3, 4, 5], 2]
expected = [1, 2, 3, 5]
```

### Case 2

```python
args = [[1], 1]
expected = []
```

### Case 3

```python
args = [[1, 2], 1]
expected = [1]
```

### Case 4

```python
args = [[1, 2], 2]
expected = [2]
```

### Case 5

```python
args = [[1, 2, 3], 3]
expected = [2, 3]
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run remove-nth-node-from-end-of-list
```
