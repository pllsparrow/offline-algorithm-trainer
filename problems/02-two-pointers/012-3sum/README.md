# 012. 3Sum

- Chapter: 02. Two Pointers
- Difficulty: Medium
- Source: https://leetcode.com/problems/3sum/
- Reference: https://neetcode.io/problems/three-integer-sum?list=neetcode150

## Goal

Classic interview problem for 3Sum. Practice left/right pointers and sorted array scanning. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: left/right pointers.
- Before coding, state the invariant or state definition: sorted array scanning.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [[-1, 0, 1, 2, -1, -4]]
expected = [[-1, -1, 2], [-1, 0, 1]]
```

### Case 2

```python
args = [[0, 1, 1]]
expected = []
```

### Case 3

```python
args = [[0, 0, 0]]
expected = [[0, 0, 0]]
```

### Case 4

```python
args = [[-1, 0, 1]]
expected = [[-1, 0, 1]]
```

### Case 5

```python
args = [[1, 2, -2, -1]]
expected = []
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run 3sum
```
