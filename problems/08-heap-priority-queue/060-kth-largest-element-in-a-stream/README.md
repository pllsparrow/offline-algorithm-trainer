# 060. Kth Largest Element In a Stream

- Chapter: 08. Heap / Priority Queue
- Difficulty: Easy
- Source: https://leetcode.com/problems/kth-largest-element-in-a-stream/
- Reference: https://neetcode.io/problems/kth-largest-integer-in-a-stream?list=neetcode150

## Goal

Classic interview problem for Kth Largest Element In a Stream. Practice Top K and two heaps. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: Top K.
- Before coding, state the invariant or state definition: two heaps.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

first line q (operations), then q lines of 'op args...'. Output: one result per operation (null for void; space-separated values for lists)

## Local Examples

### Case 1

**Input**

```
6
KthLargest 3 4 4 5 8 2
add 3
add 5
add 10
add 9
add 4
```

**Output**

```
null
4
5
5
8
8
```

### Case 2

**Input**

```
5
KthLargest 4 6 7 7 7 7 8 3
add 2
add 10
add 9
add 9
```

**Output**

```
null
7
7
7
8
```

### Case 3

**Input**

```
4
KthLargest 1 1 5
add 2
add 3
add 1
```

**Output**

```
null
5
5
5
```

## Run

```bash
python3 train.py run kth-largest-element-in-a-stream
```
