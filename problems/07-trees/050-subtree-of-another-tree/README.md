# 050. Subtree of Another Tree

- Chapter: 07. Trees
- Difficulty: Easy
- Source: https://leetcode.com/problems/subtree-of-another-tree/
- Reference: https://neetcode.io/problems/subtree-of-a-binary-tree?list=neetcode150

## Goal

Classic interview problem for Subtree of Another Tree. Practice recursive return-value design and DFS/BFS. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: recursive return-value design.
- Before coding, state the invariant or state definition: DFS/BFS.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [[3, 4, 5, 1, 2], [4, 1, 2]]
expected = True
```

### Case 2

```python
args = [[3, 4, 5, 1, 2, None, None, None, None, 0], [4, 1, 2]]
expected = False
```

### Case 3

```python
args = [[1], [1]]
expected = True
```

### Case 4

```python
args = [[1], [2]]
expected = False
```

### Case 5

```python
args = [[1, 2, 3], [2]]
expected = True
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run subtree-of-another-tree
```
