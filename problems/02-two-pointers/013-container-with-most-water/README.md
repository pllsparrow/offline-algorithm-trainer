# 013. Container With Most Water

- Chapter: 02. Two Pointers
- Difficulty: Medium
- Source: https://leetcode.com/problems/container-with-most-water/
- Reference: https://neetcode.io/problems/max-water-container?list=neetcode150

## Goal

Classic interview problem for Container With Most Water. Practice left/right pointers and sorted array scanning. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: left/right pointers.
- Before coding, state the invariant or state definition: sorted array scanning.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: height: an integer list: count n then n integers. Output: the integer.

## Local Examples

### Case 1

**Input**

```
9
1 8 6 2 5 4 8 3 7
```

**Output**

```
49
```

### Case 2

**Input**

```
2
1 1
```

**Output**

```
1
```

### Case 3

**Input**

```
3
1 2 1
```

**Output**

```
2
```

## Run

```bash
python3 train.py run container-with-most-water
```
