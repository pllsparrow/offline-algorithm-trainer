# 148. Missing Number

- Chapter: 18. Bit Manipulation
- Difficulty: Easy
- Source: https://leetcode.com/problems/missing-number/
- Reference: https://neetcode.io/problems/missing-number?list=neetcode150

## Goal

Classic interview problem for Missing Number. Practice bit manipulation tricks and XOR properties. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: bit manipulation tricks.
- Before coding, state the invariant or state definition: XOR properties.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: nums: an integer list: count n then n integers. Output: the integer.

## Local Examples

### Case 1

**Input**

```
3
3 0 1
```

**Output**

```
2
```

### Case 2

**Input**

```
2
0 1
```

**Output**

```
2
```

### Case 3

**Input**

```
9
9 6 4 2 3 5 7 0 1
```

**Output**

```
8
```

## Run

```bash
python3 train.py run missing-number
```
