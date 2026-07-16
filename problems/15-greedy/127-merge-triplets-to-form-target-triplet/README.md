# 127. Merge Triplets to Form Target Triplet

- Chapter: 15. Greedy
- Difficulty: Medium
- Source: https://leetcode.com/problems/merge-triplets-to-form-target-triplet/
- Reference: https://neetcode.io/problems/merge-triplets-to-form-target?list=neetcode150

## Goal

Classic interview problem for Merge Triplets to Form Target Triplet. Practice local optimality proofs and interval/jump strategies. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: local optimality proofs.
- Before coding, state the invariant or state definition: interval/jump strategies.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [[[2, 5, 3], [1, 8, 4], [1, 7, 5]], [2, 7, 5]]
expected = True
```

### Case 2

```python
args = [[[3, 4, 5], [4, 5, 6]], [3, 2, 5]]
expected = False
```

### Case 3

```python
args = [[[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]], [5, 5, 5]]
expected = True
```

### Case 4

```python
args = [[[1, 1, 1]], [1, 1, 1]]
expected = True
```

### Case 5

```python
args = [[[1, 1, 1]], [2, 2, 2]]
expected = False
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run merge-triplets-to-form-target-triplet
```
