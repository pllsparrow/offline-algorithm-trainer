# 052. Binary Tree Level Order Traversal

- Chapter: 07. Trees
- Difficulty: Medium
- Source: https://leetcode.com/problems/binary-tree-level-order-traversal/
- Reference: https://neetcode.io/problems/level-order-traversal-of-binary-tree?list=neetcode150

## Goal

Classic interview problem for Binary Tree Level Order Traversal. Practice recursive return-value design and DFS/BFS. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: recursive return-value design.
- Before coding, state the invariant or state definition: DFS/BFS.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [[3, 9, 20, None, None, 15, 7]]
expected = [[3], [9, 20], [15, 7]]
```

### Case 2

```python
args = [[1]]
expected = [[1]]
```

### Case 3

```python
args = [[]]
expected = []
```

### Case 4

```python
args = [[1, 2, 3, 4, 5, 6, 7]]
expected = [[1], [2, 3], [4, 5, 6, 7]]
```

### Case 5

```python
args = [[1, 2, None, 3, None, 4, None, 5]]
expected = [[1], [2], [3], [4], [5]]
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run binary-tree-level-order-traversal
```
