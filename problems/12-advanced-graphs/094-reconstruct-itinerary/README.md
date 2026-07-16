# 094. Reconstruct Itinerary

- Chapter: 12. Advanced Graphs
- Difficulty: Hard
- Source: https://leetcode.com/problems/reconstruct-itinerary/
- Reference: https://neetcode.io/problems/reconstruct-flight-path?list=neetcode150

## Goal

Classic interview problem for Reconstruct Itinerary. Practice shortest paths and minimum spanning trees. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: shortest paths.
- Before coding, state the invariant or state definition: minimum spanning trees.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [[['MUC', 'LHR'], ['JFK', 'MUC'], ['SFO', 'SJC'], ['LHR', 'SFO']]]
expected = ['JFK', 'MUC', 'LHR', 'SFO', 'SJC']
```

### Case 2

```python
args = [[['JFK', 'SFO'], ['JFK', 'ATL'], ['SFO', 'ATL'], ['ATL', 'JFK'], ['ATL', 'SFO']]]
expected = ['JFK', 'ATL', 'JFK', 'SFO', 'ATL', 'SFO']
```

### Case 3

```python
args = [[['JFK', 'AAA'], ['AAA', 'JFK'], ['JFK', 'BBB'], ['BBB', 'JFK']]]
expected = ['JFK', 'AAA', 'JFK', 'BBB', 'JFK']
```

### Case 4

```python
args = [[['JFK', 'LAX']]]
expected = ['JFK', 'LAX']
```

### Case 5

```python
args = [[['JFK', 'KKK'], ['KKK', 'LLL']]]
expected = ['JFK', 'KKK', 'LLL']
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run reconstruct-itinerary
```
