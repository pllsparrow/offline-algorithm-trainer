# 096. Swim In Rising Water

- Chapter: 12. Advanced Graphs
- Difficulty: Hard
- Source: https://leetcode.com/problems/swim-in-rising-water/
- Reference: https://neetcode.io/problems/swim-in-rising-water?list=neetcode150

## Goal

Classic interview problem for Swim In Rising Water. Practice shortest paths and minimum spanning trees. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: shortest paths.
- Before coding, state the invariant or state definition: minimum spanning trees.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [[[0, 2], [1, 3]]]
expected = 3
```

### Case 2

```python
args = [[[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]]
expected = 16
```

### Case 3

```python
args = [[[0]]]
expected = 0
```

### Case 4

```python
args = [[[5]]]
expected = 5
```

### Case 5

```python
args = [[[0, 1], [2, 3]]]
expected = 3
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run swim-in-rising-water
```
