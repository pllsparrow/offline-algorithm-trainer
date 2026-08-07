# 065. Design Twitter

- Chapter: 08. Heap / Priority Queue
- Difficulty: Medium
- Source: https://leetcode.com/problems/design-twitter/
- Reference: https://neetcode.io/problems/design-twitter-feed?list=neetcode150

## Goal

Classic interview problem for Design Twitter. Practice Top K and two heaps. Start with a brute-force idea, then optimize to an interview-ready complexity.

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
8
Twitter
postTweet 1 5
getNewsFeed 1
follow 1 2
postTweet 2 6
getNewsFeed 1
unfollow 1 2
getNewsFeed 1
```

**Output**

```
null
null
5
null
null
6 5
null
5
```

### Case 2

**Input**

```
5
Twitter
postTweet 1 1
postTweet 1 2
postTweet 1 3
getNewsFeed 1
```

**Output**

```
null
null
null
null
3 2 1
```

### Case 3

**Input**

```
5
Twitter
postTweet 1 10
postTweet 2 20
follow 1 2
getNewsFeed 1
```

**Output**

```
null
null
null
null
20 10
```

## Run

```bash
python3 train.py run design-twitter
```
