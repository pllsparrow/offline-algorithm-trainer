# 044. Reverse Nodes In K Group

- Chapter: 06. Linked List
- Difficulty: Hard
- Source: https://leetcode.com/problems/reverse-nodes-in-k-group/
- Reference: https://neetcode.io/problems/reverse-nodes-in-k-group?list=neetcode150

## Goal

Classic interview problem for Reverse Nodes In K Group. Practice pointer rewiring and fast and slow pointers. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: pointer rewiring.
- Before coding, state the invariant or state definition: fast and slow pointers.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [[1, 2, 3, 4, 5], 2]
expected = [2, 1, 4, 3, 5]
```

### Case 2

```python
args = [[1, 2, 3, 4, 5], 3]
expected = [3, 2, 1, 4, 5]
```

### Case 3

```python
args = [[1, 2, 3, 4, 5], 1]
expected = [1, 2, 3, 4, 5]
```

### Case 4

```python
args = [[1, 2, 3, 4, 5], 5]
expected = [5, 4, 3, 2, 1]
```

### Case 5

```python
args = [[1], 1]
expected = [1]
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run reverse-nodes-in-k-group
```
