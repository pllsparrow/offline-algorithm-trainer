# 093. Network Delay Time

- Chapter: 12. Advanced Graphs
- Difficulty: Medium
- Source: https://leetcode.com/problems/network-delay-time/
- Reference: https://neetcode.io/problems/network-delay-time?list=neetcode150

## Goal

Classic interview problem for Network Delay Time. Practice shortest paths and minimum spanning trees. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: shortest paths.
- Before coding, state the invariant or state definition: minimum spanning trees.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [[[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2]
expected = 2
```

### Case 2

```python
args = [[[1, 2, 1]], 2, 1]
expected = 1
```

### Case 3

```python
args = [[[1, 2, 1]], 2, 2]
expected = -1
```

### Case 4

```python
args = [[], 1, 1]
expected = 0
```

### Case 5

```python
args = [[[1, 2, 1], [2, 3, 1], [3, 4, 1]], 4, 1]
expected = 3
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run network-delay-time
```
