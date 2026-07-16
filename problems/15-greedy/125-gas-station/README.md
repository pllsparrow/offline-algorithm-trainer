# 125. Gas Station

- Chapter: 15. Greedy
- Difficulty: Medium
- Source: https://leetcode.com/problems/gas-station/
- Reference: https://neetcode.io/problems/gas-station?list=neetcode150

## Goal

Classic interview problem for Gas Station. Practice local optimality proofs and interval/jump strategies. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: local optimality proofs.
- Before coding, state the invariant or state definition: interval/jump strategies.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [[1, 2, 3, 4, 5], [3, 4, 5, 1, 2]]
expected = 3
```

### Case 2

```python
args = [[2, 3, 4], [3, 4, 3]]
expected = -1
```

### Case 3

```python
args = [[1, 2], [2, 1]]
expected = 1
```

### Case 4

```python
args = [[5], [4]]
expected = 0
```

### Case 5

```python
args = [[2], [2]]
expected = 0
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run gas-station
```
