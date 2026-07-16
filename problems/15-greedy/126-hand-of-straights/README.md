# 126. Hand of Straights

- Chapter: 15. Greedy
- Difficulty: Medium
- Source: https://leetcode.com/problems/hand-of-straights/
- Reference: https://neetcode.io/problems/hand-of-straights?list=neetcode150

## Goal

Classic interview problem for Hand of Straights. Practice local optimality proofs and interval/jump strategies. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: local optimality proofs.
- Before coding, state the invariant or state definition: interval/jump strategies.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [[1, 2, 3, 6, 2, 3, 4, 7, 8], 3]
expected = True
```

### Case 2

```python
args = [[1, 2, 3, 4, 5], 4]
expected = False
```

### Case 3

```python
args = [[1], 1]
expected = True
```

### Case 4

```python
args = [[1, 2, 3], 1]
expected = True
```

### Case 5

```python
args = [[1, 2, 3, 4], 2]
expected = True
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run hand-of-straights
```
