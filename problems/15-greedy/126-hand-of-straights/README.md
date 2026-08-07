# 126. Hand of Straights

- Chapter: 15. Greedy
- Difficulty: Medium
- Source: https://leetcode.com/problems/hand-of-straights/
- Reference: https://neetcode.io/problems/hand-of-straights?list=neetcode150

## Goal

Classic interview problem for Hand of Straights. Practice local optimality proofs and interval/jump strategies. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: local optimality proofs.
- Before coding, state the invariant or state definition: interval/jump strategies.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: arg1: an integer list: count n then n integers; arg2: an integer. Output: 1 if true else 0.

## Local Examples

### Case 1

**Input**

```
9
1 2 3 6 2 3 4 7 8
3
```

**Output**

```
1
```

### Case 2

**Input**

```
5
1 2 3 4 5
4
```

**Output**

```
0
```

### Case 3

**Input**

```
1
1
1
```

**Output**

```
1
```

## Run

```bash
python3 train.py run hand-of-straights
```
