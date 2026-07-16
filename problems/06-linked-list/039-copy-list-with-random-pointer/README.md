# 039. Copy List With Random Pointer

- Chapter: 06. Linked List
- Difficulty: Medium
- Source: https://leetcode.com/problems/copy-list-with-random-pointer/
- Reference: https://neetcode.io/problems/copy-linked-list-with-random-pointer?list=neetcode150

## Goal

Classic interview problem for Copy List With Random Pointer. Practice pointer rewiring and fast and slow pointers. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: pointer rewiring.
- Before coding, state the invariant or state definition: fast and slow pointers.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [[[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]]
expected = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
```

### Case 2

```python
args = [[[1, 1], [2, 1]]]
expected = [[1, 1], [2, 1]]
```

### Case 3

```python
args = [[[3, None], [3, 0], [3, None]]]
expected = [[3, None], [3, 0], [3, None]]
```

### Case 4

```python
args = [[]]
expected = []
```

### Case 5

```python
args = [[[1, None]]]
expected = [[1, None]]
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run copy-list-with-random-pointer
```
