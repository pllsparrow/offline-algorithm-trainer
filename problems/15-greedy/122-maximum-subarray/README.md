# 122. Maximum Subarray

- Chapter: 15. Greedy
- Difficulty: Medium
- Source: https://leetcode.com/problems/maximum-subarray/
- Reference: https://neetcode.io/problems/maximum-subarray?list=neetcode150

## Goal

Find the maximum sum of a contiguous subarray. Practice Kadane's algorithm and local state transitions.

## Interview Focus

- Identify the core pattern: local optimality proofs.
- Before coding, state the invariant or state definition: interval/jump strategies.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [[-2, 1, -3, 4, -1, 2, 1, -5, 4]]
expected = 6
```

### Case 2

```python
args = [[1]]
expected = 1
```

### Case 3

```python
args = [[5, 4, -1, 7, 8]]
expected = 23
```

### Case 4

```python
args = [[-1]]
expected = -1
```

### Case 5

```python
args = [[-2, -1]]
expected = -1
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run maximum-subarray
```
