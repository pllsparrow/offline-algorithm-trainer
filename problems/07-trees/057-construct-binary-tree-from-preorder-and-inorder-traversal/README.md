# 057. Construct Binary Tree From Preorder And Inorder Traversal

- Chapter: 07. Trees
- Difficulty: Medium
- Source: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
- Reference: https://neetcode.io/problems/binary-tree-from-preorder-and-inorder-traversal?list=neetcode150

## Goal

Classic interview problem for Construct Binary Tree From Preorder And Inorder Traversal. Practice recursive return-value design and DFS/BFS. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: recursive return-value design.
- Before coding, state the invariant or state definition: DFS/BFS.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [[], []]
expected = []
```

### Case 2

```python
args = [[1], [1]]
expected = [1]
```

### Case 3

```python
args = [[3, 9, 20, 15, 7], [9, 3, 15, 20, 7]]
expected = [3, 9, 20, None, None, 15, 7]
```

### Case 4

```python
args = [[-1], [-1]]
expected = [-1]
```

### Case 5

```python
args = [[1, 2], [2, 1]]
expected = [1, 2]
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run construct-binary-tree-from-preorder-and-inorder-traversal
```
