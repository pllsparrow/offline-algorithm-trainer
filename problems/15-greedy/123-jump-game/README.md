# 123. Jump Game

- Chapter: 15. Greedy
- Difficulty: Medium
- Source: https://leetcode.com/problems/jump-game/
- Reference: https://neetcode.io/problems/jump-game?list=neetcode150

## Goal

Classic interview problem for Jump Game. Practice local optimality proofs and interval/jump strategies. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: local optimality proofs.
- Before coding, state the invariant or state definition: interval/jump strategies.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: nums: an integer list: count n then n integers. Output: 1 if true else 0.

## Local Examples

### Case 1

**Input**

```
5
2 3 1 1 4
```

**Output**

```
1
```

### Case 2

**Input**

```
5
3 2 1 0 4
```

**Output**

```
0
```

### Case 3

**Input**

```
1
0
```

**Output**

```
1
```

## Run

```bash
python3 train.py run jump-game
```
