# 007. Product of Array Except Self

- Chapter: 01. Arrays & Hashing
- Difficulty: Medium
- Source: https://leetcode.com/problems/product-of-array-except-self/
- Reference: https://neetcode.io/problems/products-of-array-discluding-self?list=neetcode150

## Goal

Classic interview problem for Product of Array Except Self. Practice hash table modeling and frequency counting. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: hash table modeling.
- Before coding, state the invariant or state definition: frequency counting.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [[1, 2, 3, 4]]
expected = [24, 12, 8, 6]
```

### Case 2

```python
args = [[-1, 1, 0, -3, 3]]
expected = [0, 0, 9, 0, 0]
```

### Case 3

```python
args = [[2, 3, 4, 5]]
expected = [60, 40, 30, 24]
```

### Case 4

```python
args = [[1, 1]]
expected = [1, 1]
```

### Case 5

```python
args = [[5, 2]]
expected = [2, 5]
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run product-of-array-except-self
```
