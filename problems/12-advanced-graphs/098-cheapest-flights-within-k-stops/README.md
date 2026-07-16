# 098. Cheapest Flights Within K Stops

- Chapter: 12. Advanced Graphs
- Difficulty: Medium
- Source: https://leetcode.com/problems/cheapest-flights-within-k-stops/
- Reference: https://neetcode.io/problems/cheapest-flight-path?list=neetcode150

## Goal

Classic interview problem for Cheapest Flights Within K Stops. Practice shortest paths and minimum spanning trees. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: shortest paths.
- Before coding, state the invariant or state definition: minimum spanning trees.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1]
expected = 700
```

### Case 2

```python
args = [3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1]
expected = 200
```

### Case 3

```python
args = [3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0]
expected = 500
```

### Case 4

```python
args = [5, [[0, 1, 100], [0, 2, 500], [1, 2, 100], [1, 3, 600], [2, 3, 200], [3, 4, 100]], 0, 4, 2]
expected = 800
```

### Case 5

```python
args = [4, [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]], 0, 3, 1]
expected = 6
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run cheapest-flights-within-k-stops
```
