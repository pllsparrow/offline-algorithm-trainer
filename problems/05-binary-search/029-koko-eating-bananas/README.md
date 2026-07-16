# 029. Koko Eating Bananas

- Chapter: 05. Binary Search
- Difficulty: Medium
- Source: https://leetcode.com/problems/koko-eating-bananas/
- Reference: https://neetcode.io/problems/eating-bananas?list=neetcode150

## Goal

Classic interview problem for Koko Eating Bananas. Practice search space definition and boundary shrinking. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: search space definition.
- Before coding, state the invariant or state definition: boundary shrinking.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [[3, 6, 7, 11], 8]
expected = 4
```

### Case 2

```python
args = [[30, 11, 23, 4, 20], 5]
expected = 30
```

### Case 3

```python
args = [[30, 11, 23, 4, 20], 6]
expected = 23
```

### Case 4

```python
args = [[1], 1]
expected = 1
```

### Case 5

```python
args = [[5], 5]
expected = 1
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run koko-eating-bananas
```
