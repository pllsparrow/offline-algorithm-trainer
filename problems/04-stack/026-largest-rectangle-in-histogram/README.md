# 026. Largest Rectangle In Histogram

- Chapter: 04. Stack
- Difficulty: Hard
- Source: https://leetcode.com/problems/largest-rectangle-in-histogram/
- Reference: https://neetcode.io/problems/largest-rectangle-in-histogram?list=neetcode150

## Goal

Classic interview problem for Largest Rectangle In Histogram. Practice monotonic stacks and parentheses matching. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: monotonic stacks.
- Before coding, state the invariant or state definition: parentheses matching.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: heights: an integer list: count n then n integers. Output: the integer.

## Local Examples

### Case 1

**Input**

```
6
2 1 5 6 2 3
```

**Output**

```
10
```

### Case 2

**Input**

```
2
2 4
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
python3 train.py run largest-rectangle-in-histogram
```
