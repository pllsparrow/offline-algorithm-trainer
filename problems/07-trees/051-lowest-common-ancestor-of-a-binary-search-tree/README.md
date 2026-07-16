# 051. Lowest Common Ancestor of a Binary Search Tree

- Chapter: 07. Trees
- Difficulty: Medium
- Source: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
- Reference: https://neetcode.io/problems/lowest-common-ancestor-in-binary-search-tree?list=neetcode150

## Goal

Classic interview problem for Lowest Common Ancestor of a Binary Search Tree. Practice recursive return-value design and DFS/BFS. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: recursive return-value design.
- Before coding, state the invariant or state definition: DFS/BFS.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [[6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 8]
expected = 6
```

### Case 2

```python
args = [[6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 4]
expected = 2
```

### Case 3

```python
args = [[2, 1], 2, 1]
expected = 2
```

### Case 4

```python
args = [[2, 1], 1, 2]
expected = 2
```

### Case 5

```python
args = [[6, 2, 8, 0, 4, 7, 9], 0, 4]
expected = 2
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run lowest-common-ancestor-of-a-binary-search-tree
```
