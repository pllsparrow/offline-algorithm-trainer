# 098. Cheapest Flights Within K Stops

- Chapter: 12. Advanced Graphs
- Difficulty: Medium
- Source: https://leetcode.com/problems/cheapest-flights-within-k-stops/
- Reference: https://neetcode.io/problems/cheapest-flight-path?list=neetcode150

## Goal

Classic interview problem for Cheapest Flights Within K Stops. Practice shortest paths and minimum spanning trees. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: shortest paths.
- Before coding, state the invariant or state definition: minimum spanning trees.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: n: an integer; flights: edges3: count then values; src: an integer; dst: an integer; k: an integer. Output: the integer.

## Local Examples

### Case 1

**Input**

```
4
5
0 1 100
1 2 100
2 0 100
1 3 600
2 3 200
0
3
1
```

**Output**

```
700
```

### Case 2

**Input**

```
3
3
0 1 100
1 2 100
0 2 500
0
2
1
```

**Output**

```
200
```

### Case 3

**Input**

```
3
3
0 1 100
1 2 100
0 2 500
0
2
0
```

**Output**

```
500
```

## Run

```bash
python3 train.py run cheapest-flights-within-k-stops
```
