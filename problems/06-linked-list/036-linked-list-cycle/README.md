# 036. Linked List Cycle

- Chapter: 06. Linked List
- Difficulty: Easy
- Source: https://leetcode.com/problems/linked-list-cycle/
- Reference: https://neetcode.io/problems/linked-list-cycle-detection?list=neetcode150

## Goal

Classic interview problem for Linked List Cycle. Practice pointer rewiring and fast and slow pointers. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: pointer rewiring.
- Before coding, state the invariant or state definition: fast and slow pointers.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [[3, 2, 0, -4], 1]
expected = True
```

### Case 2

```python
args = [[1, 2], 0]
expected = True
```

### Case 3

```python
args = [[1], -1]
expected = False
```

### Case 4

```python
args = [[], -1]
expected = False
```

### Case 5

```python
args = [[1, 2, 3], -1]
expected = False
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run linked-list-cycle
```
