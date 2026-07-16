# 041. Find The Duplicate Number

- Chapter: 06. Linked List
- Difficulty: Medium
- Source: https://leetcode.com/problems/find-the-duplicate-number/
- Reference: https://neetcode.io/problems/find-duplicate-integer?list=neetcode150

## Goal

Classic interview problem for Find The Duplicate Number. Practice pointer rewiring and fast and slow pointers. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: pointer rewiring.
- Before coding, state the invariant or state definition: fast and slow pointers.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [[1, 3, 4, 2, 2]]
expected = 2
```

### Case 2

```python
args = [[3, 1, 3, 4, 2]]
expected = 3
```

### Case 3

```python
args = [[3, 3, 3, 3, 3]]
expected = 3
```

### Case 4

```python
args = [[1, 1]]
expected = 1
```

### Case 5

```python
args = [[2, 2, 2]]
expected = 2
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run find-the-duplicate-number
```
