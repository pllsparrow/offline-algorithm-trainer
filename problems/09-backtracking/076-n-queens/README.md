# 076. N Queens

- Chapter: 09. Backtracking
- Difficulty: Hard
- Source: https://leetcode.com/problems/n-queens/
- Reference: https://neetcode.io/problems/n-queens?list=neetcode150

## Goal

Classic interview problem for N Queens. Practice choice paths and pruning. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: choice paths.
- Before coding, state the invariant or state definition: pruning.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = [1]
expected = [['Q']]
```

### Case 2

```python
args = [2]
expected = []
```

### Case 3

```python
args = [3]
expected = []
```

### Case 4

```python
args = [4]
expected = [['..Q.', 'Q...', '...Q', '.Q..'], ['.Q..', '...Q', 'Q...', '..Q.']]
```

### Case 5

```python
args = [5]
expected = [['....Q', '..Q..', 'Q....', '...Q.', '.Q...'], ['....Q', '.Q...', '...Q.', 'Q....', '..Q..'], ['...Q.', '.Q...', '....Q', '..Q..', 'Q....'], ['...Q.', 'Q....', '..Q..', '....Q', '.Q...'], ['..Q..', '....Q', '.Q...', '...Q.', 'Q....'], ['..Q..', 'Q....', '...Q.', '.Q...', '....Q'], ['.Q...', '....Q', '..Q..', 'Q....', '...Q.'], ['.Q...', '...Q.', 'Q....', '..Q..', '....Q'], ['Q....', '...Q.', '.Q...', '....Q', '..Q..'], ['Q....', '..Q..', '....Q', '.Q...', '...Q.']]
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run n-queens
```
