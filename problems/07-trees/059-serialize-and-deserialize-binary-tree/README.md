# 059. Serialize And Deserialize Binary Tree

- Chapter: 07. Trees
- Difficulty: Hard
- Source: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
- Reference: https://neetcode.io/problems/serialize-and-deserialize-binary-tree?list=neetcode150

## Goal

Classic interview problem for Serialize And Deserialize Binary Tree. Practice recursive return-value design and DFS/BFS. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: recursive return-value design.
- Before coding, state the invariant or state definition: DFS/BFS.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [[1, 2, 3, None, None, 4, 5]]
expected = [1, 2, 3, None, None, 4, 5]
```

### Case 2

```python
args = [[]]
expected = []
```

### Case 3

```python
args = [[1]]
expected = [1]
```

### Case 4

```python
args = [[1, 2]]
expected = [1, 2]
```

### Case 5

```python
args = [[1, None, 2]]
expected = [1, None, 2]
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run serialize-and-deserialize-binary-tree
```
