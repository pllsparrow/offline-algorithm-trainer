# 023. Evaluate Reverse Polish Notation

- Chapter: 04. Stack
- Difficulty: Medium
- Source: https://leetcode.com/problems/evaluate-reverse-polish-notation/
- Reference: https://neetcode.io/problems/evaluate-reverse-polish-notation?list=neetcode150

## Goal

Classic interview problem for Evaluate Reverse Polish Notation. Practice monotonic stacks and parentheses matching. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: monotonic stacks.
- Before coding, state the invariant or state definition: parentheses matching.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: arg1: a string list: count n then n tokens. Output: the integer.

## Local Examples

### Case 1

**Input**

```
5
2
1
+
3
*
```

**Output**

```
9
```

### Case 2

**Input**

```
5
4
13
5
/
+
```

**Output**

```
6
```

### Case 3

**Input**

```
13
10
6
9
3
+
-11
*
/
*
17
+
5
+
```

**Output**

```
22
```

## Run

```bash
python3 train.py run evaluate-reverse-polish-notation
```
