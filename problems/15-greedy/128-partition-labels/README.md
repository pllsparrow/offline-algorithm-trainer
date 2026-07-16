# 128. Partition Labels

- Chapter: 15. Greedy
- Difficulty: Medium
- Source: https://leetcode.com/problems/partition-labels/
- Reference: https://neetcode.io/problems/partition-labels?list=neetcode150

## Goal

Classic interview problem for Partition Labels. Practice local optimality proofs and interval/jump strategies. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: local optimality proofs.
- Before coding, state the invariant or state definition: interval/jump strategies.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = ['ababcbacadefegdehijhklij']
expected = [9, 7, 8]
```

### Case 2

```python
args = ['eccbbbbdec']
expected = [10]
```

### Case 3

```python
args = ['a']
expected = [1]
```

### Case 4

```python
args = ['ab']
expected = [1, 1]
```

### Case 5

```python
args = ['aaa']
expected = [3]
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run partition-labels
```
