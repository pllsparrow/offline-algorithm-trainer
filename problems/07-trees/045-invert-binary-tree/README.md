# 045. Invert Binary Tree

- Chapter: 07. Trees
- Difficulty: Easy
- Source: https://leetcode.com/problems/invert-binary-tree/
- Reference: https://neetcode.io/problems/invert-a-binary-tree?list=neetcode150

## Goal

Invert a binary tree. Practice recursively processing left and right subtrees.

## Interview Focus

- Identify the core pattern: recursive return-value design.
- Before coding, state the invariant or state definition: DFS/BFS.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [[4, 2, 7, 1, 3, 6, 9]]
expected = [4, 7, 2, 9, 6, 3, 1]
```

### Case 2

```python
args = [[2, 1, 3]]
expected = [2, 3, 1]
```

### Case 3

```python
args = [[]]
expected = []
```

### Case 4

```python
args = [[1]]
expected = [1]
```

### Case 5

```python
args = [[1, 2]]
expected = [1, None, 2]
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run invert-binary-tree
```
