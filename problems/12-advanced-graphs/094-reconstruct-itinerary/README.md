# 094. Reconstruct Itinerary

- Chapter: 12. Advanced Graphs
- Difficulty: Hard
- Source: https://leetcode.com/problems/reconstruct-itinerary/
- Reference: https://neetcode.io/problems/reconstruct-flight-path?list=neetcode150

## Goal

Classic interview problem for Reconstruct Itinerary. Practice shortest paths and minimum spanning trees. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: shortest paths.
- Before coding, state the invariant or state definition: minimum spanning trees.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: arg1: string pairs: count m then m lines of two tokens. Output: the strings space-separated.

## Local Examples

### Case 1

**Input**

```
4
MUC LHR
JFK MUC
SFO SJC
LHR SFO
```

**Output**

```
JFK MUC LHR SFO SJC
```

### Case 2

**Input**

```
5
JFK SFO
JFK ATL
SFO ATL
ATL JFK
ATL SFO
```

**Output**

```
JFK ATL JFK SFO ATL SFO
```

### Case 3

**Input**

```
4
JFK AAA
AAA JFK
JFK BBB
BBB JFK
```

**Output**

```
JFK AAA JFK BBB JFK
```

## Run

```bash
python3 train.py run reconstruct-itinerary
```
