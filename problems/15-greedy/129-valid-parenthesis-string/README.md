# 129. Valid Parenthesis String

- Chapter: 15. Greedy
- Difficulty: Medium
- Source: https://leetcode.com/problems/valid-parenthesis-string/
- Reference: https://neetcode.io/problems/valid-parenthesis-string?list=neetcode150

## Goal

Classic interview problem for Valid Parenthesis String. Practice local optimality proofs and interval/jump strategies. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: local optimality proofs.
- Before coding, state the invariant or state definition: interval/jump strategies.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: arg1: a string token. Output: 1 if true else 0.

## Local Examples

### Case 1

**Input**

```
()
```

**Output**

```
1
```

### Case 2

**Input**

```
(*)
```

**Output**

```
1
```

### Case 3

**Input**

```
(*))
```

**Output**

```
1
```

## Run

```bash
python3 train.py run valid-parenthesis-string
```
