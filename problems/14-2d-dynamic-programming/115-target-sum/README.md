# 115. Target Sum

- Chapter: 14. 2-D Dynamic Programming
- Difficulty: Medium
- Source: https://leetcode.com/problems/target-sum/
- Reference: https://neetcode.io/problems/target-sum?list=neetcode150

## Goal

Classic interview problem for Target Sum. Practice 2D state design and string DP. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: 2D state design.
- Before coding, state the invariant or state definition: string DP.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [[1, 1, 1, 1, 1], 3]
expected = 5
```

### Case 2

```python
args = [[1], 1]
expected = 1
```

### Case 3

```python
args = [[1], 2]
expected = 0
```

### Case 4

```python
args = [[0, 0, 0, 0, 0, 0, 0, 0, 0], 0]
expected = 512
```

### Case 5

```python
args = [[1000], -1000]
expected = 1
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run target-sum
```
