# 147. Reverse Bits

- Chapter: 18. Bit Manipulation
- Difficulty: Easy
- Source: https://leetcode.com/problems/reverse-bits/
- Reference: https://neetcode.io/problems/reverse-bits?list=neetcode150

## Goal

Classic interview problem for Reverse Bits. Practice bit manipulation tricks and XOR properties. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: bit manipulation tricks.
- Before coding, state the invariant or state definition: XOR properties.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: n: an integer. Output: the integer.

## Local Examples

### Case 1

**Input**

```
43261596
```

**Output**

```
964176192
```

### Case 2

**Input**

```
2147483644
```

**Output**

```
1073741822
```

### Case 3

**Input**

```
0
```

**Output**

```
0
```

## Run

```bash
python3 train.py run reverse-bits
```
