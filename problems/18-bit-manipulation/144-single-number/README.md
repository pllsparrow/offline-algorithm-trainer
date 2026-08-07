# 144. Single Number

- Chapter: 18. Bit Manipulation
- Difficulty: Easy
- Source: https://leetcode.com/problems/single-number/
- Reference: https://neetcode.io/problems/single-number?list=neetcode150

## Goal

Classic interview problem for Single Number. Practice bit manipulation tricks and XOR properties. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: bit manipulation tricks.
- Before coding, state the invariant or state definition: XOR properties.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: arg1: an integer list: count n then n integers. Output: the integer.

## Local Examples

### Case 1

**Input**

```
3
2 2 1
```

**Output**

```
1
```

### Case 2

**Input**

```
5
4 1 2 1 2
```

**Output**

```
4
```

### Case 3

**Input**

```
1
1
```

**Output**

```
1
```

## Run

```bash
python3 train.py run single-number
```
