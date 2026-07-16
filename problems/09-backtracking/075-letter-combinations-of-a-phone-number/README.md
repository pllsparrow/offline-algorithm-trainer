# 075. Letter Combinations of a Phone Number

- Chapter: 09. Backtracking
- Difficulty: Medium
- Source: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
- Reference: https://neetcode.io/problems/combinations-of-a-phone-number?list=neetcode150

## Goal

Classic interview problem for Letter Combinations of a Phone Number. Practice choice paths and pruning. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: choice paths.
- Before coding, state the invariant or state definition: pruning.
- After it passes, explain the time complexity, space complexity, and one edge case.

## Local Examples

### Case 1

```python
args = ['23']
expected = ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
```

### Case 2

```python
args = ['']
expected = []
```

### Case 3

```python
args = ['2']
expected = ['a', 'b', 'c']
```

### Case 4

```python
args = ['234']
expected = ['adg', 'adh', 'adi', 'aeg', 'aeh', 'aei', 'afg', 'afh', 'afi', 'bdg', 'bdh', 'bdi', 'beg', 'beh', 'bei', 'bfg', 'bfh', 'bfi', 'cdg', 'cdh', 'cdi', 'ceg', 'ceh', 'cei', 'cfg', 'cfh', 'cfi']
```

### Case 5

```python
args = ['7']
expected = ['p', 'q', 'r', 's']
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run letter-combinations-of-a-phone-number
```
