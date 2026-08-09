# 093. Network Delay Time

- Chapter: 12. Advanced Graphs
- Difficulty: Medium
- Source: https://leetcode.com/problems/network-delay-time/
- Reference: https://neetcode.io/problems/network-delay-time?list=neetcode150

## Goal

Classic interview problem for Network Delay Time. Practice shortest paths and minimum spanning trees. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: shortest paths.
- Before coding, state the invariant or state definition: minimum spanning trees.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: times: edges3: count then values; n: an integer; k: an integer. Output: the integer.

## Local Examples

### Case 1

**Input**

```
3
2 1 1
2 3 1
3 4 1
4
2
```

**Output**

```
2
```

### Case 2

**Input**

```
1
1 2 1
2
1
```

**Output**

```
1
```

### Case 3

**Input**

```
1
1 2 1
2
2
```

**Output**

```
-1
```

## Run

```bash
python3 train.py run network-delay-time
```
