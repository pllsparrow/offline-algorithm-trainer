# 022. Min Stack

- Chapter: 04. Stack
- Difficulty: Medium
- Source: https://leetcode.com/problems/min-stack/
- Reference: https://neetcode.io/problems/minimum-stack?list=neetcode150

## Goal

Design a stack that can return the minimum value in O(1). Practice maintaining auxiliary stack state.

## Interview Focus

- Identify the core pattern: monotonic stacks.
- Before coding, state the invariant or state definition: parentheses matching.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

first line q (operations), then q lines of 'op args...'. Output: one result per operation (null for void; space-separated values for lists)

## Local Examples

### Case 1

**Input**

```
8
MinStack
push -2
push 0
push -3
getMin
pop
top
getMin
```

**Output**

```
null
null
null
null
-3
null
0
-2
```

### Case 2

**Input**

```
5
MinStack
push 5
top
getMin
pop
```

**Output**

```
null
null
5
5
null
```

### Case 3

**Input**

```
9
MinStack
push 1
push 1
push 2
getMin
pop
getMin
pop
getMin
```

**Output**

```
null
null
null
null
1
null
1
null
1
```

## Run

```bash
python3 train.py run min-stack
```
