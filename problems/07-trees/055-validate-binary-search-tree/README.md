# 055. Validate Binary Search Tree

- Chapter: 07. Trees
- Difficulty: Medium
- Source: https://leetcode.com/problems/validate-binary-search-tree/
- Reference: https://neetcode.io/problems/valid-binary-search-tree?list=neetcode150

## Goal

Classic interview problem for Validate Binary Search Tree. Practice recursive return-value design and DFS/BFS. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: recursive return-value design.
- Before coding, state the invariant or state definition: DFS/BFS.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [[2, 1, 3]]
expected = True
```

### Case 2

```python
args = [[5, 1, 4, None, None, 3, 6]]
expected = False
```

### Case 3

```python
args = [[1]]
expected = True
```

### Case 4

```python
args = [[1, 1]]
expected = False
```

### Case 5

```python
args = [[10, 5, 15, None, None, 6, 20]]
expected = False
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run validate-binary-search-tree
```
