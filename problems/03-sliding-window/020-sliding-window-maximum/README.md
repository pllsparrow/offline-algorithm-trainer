# 020. Sliding Window Maximum

- Chapter: 03. Sliding Window
- Difficulty: Hard
- Source: https://leetcode.com/problems/sliding-window-maximum/
- Reference: https://neetcode.io/problems/sliding-window-maximum?list=neetcode150

## Goal

Classic interview problem for Sliding Window Maximum. Practice window invariants and left/right boundary movement. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: window invariants.
- Before coding, state the invariant or state definition: left/right boundary movement.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: arg1: an integer list: count n then n integers; arg2: an integer. Output: the values space-separated.

## Local Examples

### Case 1

**Input**

```
8
1 3 -1 -3 5 3 6 7
3
```

**Output**

```
3 3 5 5 6 7
```

### Case 2

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

### Case 3

**Input**

```
2
1 -1
1
```

**Output**

```
1 -1
```

## Run

```bash
python3 train.py run sliding-window-maximum
```
