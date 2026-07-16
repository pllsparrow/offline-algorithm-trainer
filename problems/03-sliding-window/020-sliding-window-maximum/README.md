# 020. Sliding Window Maximum

- Chapter: 03. Sliding Window
- Difficulty: Hard
- Source: https://leetcode.com/problems/sliding-window-maximum/
- Reference: https://neetcode.io/problems/sliding-window-maximum?list=neetcode150

## Goal

Classic interview problem for Sliding Window Maximum. Practice window invariants and left/right boundary movement. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: window invariants.
- Before coding, state the invariant or state definition: left/right boundary movement.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [[1, 3, -1, -3, 5, 3, 6, 7], 3]
expected = [3, 3, 5, 5, 6, 7]
```

### Case 2

```python
args = [[1], 1]
expected = [1]
```

### Case 3

```python
args = [[1, -1], 1]
expected = [1, -1]
```

### Case 4

```python
args = [[9, 11], 2]
expected = [11]
```

### Case 5

```python
args = [[4, -2], 2]
expected = [4]
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run sliding-window-maximum
```
