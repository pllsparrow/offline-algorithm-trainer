# 095. Min Cost to Connect All Points

- Chapter: 12. Advanced Graphs
- Difficulty: Medium
- Source: https://leetcode.com/problems/min-cost-to-connect-all-points/
- Reference: https://neetcode.io/problems/min-cost-to-connect-points?list=neetcode150

## Goal

Classic interview problem for Min Cost to Connect All Points. Practice shortest paths and minimum spanning trees. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: shortest paths.
- Before coding, state the invariant or state definition: minimum spanning trees.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [[[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]]
expected = 20
```

### Case 2

```python
args = [[[3, 12], [-2, 5], [-4, 1]]]
expected = 18
```

### Case 3

```python
args = [[[0, 0]]]
expected = 0
```

### Case 4

```python
args = [[[0, 0], [1, 1]]]
expected = 2
```

### Case 5

```python
args = [[[0, 0], [1, 1], [2, 2]]]
expected = 4
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run min-cost-to-connect-all-points
```
