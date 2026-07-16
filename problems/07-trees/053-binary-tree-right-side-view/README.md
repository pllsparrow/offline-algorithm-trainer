# 053. Binary Tree Right Side View

- Chapter: 07. Trees
- Difficulty: Medium
- Source: https://leetcode.com/problems/binary-tree-right-side-view/
- Reference: https://neetcode.io/problems/binary-tree-right-side-view?list=neetcode150

## Goal

Classic interview problem for Binary Tree Right Side View. Practice recursive return-value design and DFS/BFS. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: recursive return-value design.
- Before coding, state the invariant or state definition: DFS/BFS.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [[1, 2, 3, None, 5, None, 4]]
expected = [1, 3, 4]
```

### Case 2

```python
args = [[1, 2, 3, 4, None, None, None, 5]]
expected = [1, 3, 4, 5]
```

### Case 3

```python
args = [[1, None, 3]]
expected = [1, 3]
```

### Case 4

```python
args = [[]]
expected = []
```

### Case 5

```python
args = [[1]]
expected = [1]
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run binary-tree-right-side-view
```
