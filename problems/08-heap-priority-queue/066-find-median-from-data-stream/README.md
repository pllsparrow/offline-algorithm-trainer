# 066. Find Median From Data Stream

- Chapter: 08. Heap / Priority Queue
- Difficulty: Hard
- Source: https://leetcode.com/problems/find-median-from-data-stream/
- Reference: https://neetcode.io/problems/find-median-in-a-data-stream?list=neetcode150

## Goal

Classic interview problem for Find Median From Data Stream. Practice Top K and two heaps. Start with a brute-force idea, then optimize to an interview-ready complexity.

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
MedianFinder
addNum 1
addNum 2
findMedian
addNum 3
findMedian
```

**Output**

```
null
null
null
1.5
null
2.0
```

### Case 2

**Input**

```
3
MedianFinder
addNum 1
findMedian
```

**Output**

```
null
null
1.0
```

### Case 3

**Input**

```
5
MedianFinder
addNum 1
addNum 1
addNum 1
findMedian
```

**Output**

```
null
null
null
null
1.0
```

## Run

```bash
python3 train.py run find-median-from-data-stream
```
