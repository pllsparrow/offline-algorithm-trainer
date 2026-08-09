# 087. Course Schedule

- Chapter: 11. Graphs
- Difficulty: Medium
- Source: https://leetcode.com/problems/course-schedule/
- Reference: https://neetcode.io/problems/course-schedule?list=neetcode150

## Goal

Classic interview problem for Course Schedule. Practice DFS/BFS and topological sorting. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: DFS/BFS.
- Before coding, state the invariant or state definition: topological sorting.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: num_courses: an integer; prerequisites: edges2: count then values. Output: 1 if true else 0.

## Local Examples

### Case 1

**Input**

```
2
1
1 0
```

**Output**

```
1
```

### Case 2

**Input**

```
2
2
1 0
0 1
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
python3 train.py run course-schedule
```
