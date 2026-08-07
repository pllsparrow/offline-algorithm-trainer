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

## ACM Format

Input: arg1: a string token. Output: the values space-separated in ascending order.

## Local Examples

### Case 1

**Input**

```
23
```

**Output**

```
ad ae af bd be bf cd ce cf
```

### Case 2

**Input**

```

```

**Output**

```
```

### Case 3

**Input**

```
2
```

**Output**

```
a b c
```

## Run

```bash
python3 train.py run letter-combinations-of-a-phone-number
```
