# 128. Partition Labels

- Chapter: 15. Greedy
- Difficulty: Medium
- Source: https://leetcode.com/problems/partition-labels/
- Reference: https://neetcode.io/problems/partition-labels?list=neetcode150

## Goal

Classic interview problem for Partition Labels. Practice local optimality proofs and interval/jump strategies. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: local optimality proofs.
- Before coding, state the invariant or state definition: interval/jump strategies.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: s: a string token. Output: the values space-separated in ascending order.

## Local Examples

### Case 1

**Input**

```
ababcbacadefegdehijhklij
```

**Output**

```
7 8 9
```

### Case 2

**Input**

```
eccbbbbdec
```

**Output**

```
10
```

### Case 3

**Input**

```
a
```

**Output**

```
1
```

## Run

```bash
python3 train.py run partition-labels
```
