# 029. Koko Eating Bananas

- Chapter: 05. Binary Search
- Difficulty: Medium
- Source: https://leetcode.com/problems/koko-eating-bananas/
- Reference: https://neetcode.io/problems/eating-bananas?list=neetcode150

## Goal

Classic interview problem for Koko Eating Bananas. Practice search space definition and boundary shrinking. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: search space definition.
- Before coding, state the invariant or state definition: boundary shrinking.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: piles: an integer list: count n then n integers; h: an integer. Output: the integer.

## Local Examples

### Case 1

**Input**

```
4
3 6 7 11
8
```

**Output**

```
4
```

### Case 2

**Input**

```
5
30 11 23 4 20
5
```

**Output**

```
30
```

### Case 3

**Input**

```
5
30 11 23 4 20
6
```

**Output**

```
23
```

## Run

```bash
python3 train.py run koko-eating-bananas
```
