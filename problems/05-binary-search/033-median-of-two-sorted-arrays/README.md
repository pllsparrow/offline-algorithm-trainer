# 033. Median of Two Sorted Arrays

- Chapter: 05. Binary Search
- Difficulty: Hard
- Source: https://leetcode.com/problems/median-of-two-sorted-arrays/
- Reference: https://neetcode.io/problems/median-of-two-sorted-arrays?list=neetcode150

## Goal

Classic interview problem for Median of Two Sorted Arrays. Practice search space definition and boundary shrinking. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: search space definition.
- Before coding, state the invariant or state definition: boundary shrinking.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [[1, 3], [2]]
expected = 2.0
```

### Case 2

```python
args = [[1, 2], [3, 4]]
expected = 2.5
```

### Case 3

```python
args = [[1], []]
expected = 1.0
```

### Case 4

```python
args = [[], [1]]
expected = 1.0
```

### Case 5

```python
args = [[1, 2, 3], []]
expected = 2.0
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run median-of-two-sorted-arrays
```
