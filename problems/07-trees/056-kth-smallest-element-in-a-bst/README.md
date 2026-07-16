# 056. Kth Smallest Element In a Bst

- Chapter: 07. Trees
- Difficulty: Medium
- Source: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
- Reference: https://neetcode.io/problems/kth-smallest-integer-in-bst?list=neetcode150

## Goal

Classic interview problem for Kth Smallest Element In a Bst. Practice recursive return-value design and DFS/BFS. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: recursive return-value design.
- Before coding, state the invariant or state definition: DFS/BFS.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [[3, 1, 4, None, 2], 1]
expected = 1
```

### Case 2

```python
args = [[5, 3, 6, 2, 4, None, None, 1], 3]
expected = 3
```

### Case 3

```python
args = [[1], 1]
expected = 1
```

### Case 4

```python
args = [[2, 1, 3], 2]
expected = 2
```

### Case 5

```python
args = [[4, 2, 6, 1, 3, 5, 7], 4]
expected = 4
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run kth-smallest-element-in-a-bst
```
