# 127. Merge Triplets to Form Target Triplet

- Chapter: 15. Greedy
- Difficulty: Medium
- Source: https://leetcode.com/problems/merge-triplets-to-form-target-triplet/
- Reference: https://neetcode.io/problems/merge-triplets-to-form-target?list=neetcode150

## Goal

Classic interview problem for Merge Triplets to Form Target Triplet. Practice local optimality proofs and interval/jump strategies. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: local optimality proofs.
- Before coding, state the invariant or state definition: interval/jump strategies.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: arg1: edges3: count then values; arg2: an integer list: count n then n integers. Output: 1 if true else 0.

## Local Examples

### Case 1

**Input**

```
3
2 5 3
1 8 4
1 7 5
3
2 7 5
```

**Output**

```
1
```

### Case 2

**Input**

```
2
3 4 5
4 5 6
3
3 2 5
```

**Output**

```
0
```

### Case 3

**Input**

```
4
2 5 3
2 3 4
1 2 5
5 2 3
3
5 5 5
```

**Output**

```
1
```

## Run

```bash
python3 train.py run merge-triplets-to-form-target-triplet
```
