# 092. Word Ladder

- Chapter: 11. Graphs
- Difficulty: Hard
- Source: https://leetcode.com/problems/word-ladder/
- Reference: https://neetcode.io/problems/word-ladder?list=neetcode150

## Goal

Classic interview problem for Word Ladder. Practice DFS/BFS and topological sorting. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: DFS/BFS.
- Before coding, state the invariant or state definition: topological sorting.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = ['hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']]
expected = 5
```

### Case 2

```python
args = ['hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log']]
expected = 0
```

### Case 3

```python
args = ['a', 'c', ['a', 'b', 'c']]
expected = 2
```

### Case 4

```python
args = ['hot', 'dog', ['hot', 'dog']]
expected = 0
```

### Case 5

```python
args = ['hot', 'dog', ['hot', 'hog', 'dog']]
expected = 3
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run word-ladder
```
