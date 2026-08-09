# 125. Gas Station

- Chapter: 15. Greedy
- Difficulty: Medium
- Source: https://leetcode.com/problems/gas-station/
- Reference: https://neetcode.io/problems/gas-station?list=neetcode150

## Goal

Classic interview problem for Gas Station. Practice local optimality proofs and interval/jump strategies. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: local optimality proofs.
- Before coding, state the invariant or state definition: interval/jump strategies.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: gas: an integer list: count n then n integers; cost: an integer list: count n then n integers. Output: the integer.

## Local Examples

### Case 1

**Input**

```
5
1 2 3 4 5
5
3 4 5 1 2
```

**Output**

```
3
```

### Case 2

**Input**

```
3
2 3 4
3
3 4 3
```

**Output**

```
-1
```

### Case 3

**Input**

```
2
1 2
2
2 1
```

**Output**

```
1
```

## Run

```bash
python3 train.py run gas-station
```
