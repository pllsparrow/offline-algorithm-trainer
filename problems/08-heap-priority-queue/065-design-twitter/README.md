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

## Local Examples

### Case 1

```python
ops = ['Twitter', 'postTweet', 'getNewsFeed', 'follow', 'postTweet', 'getNewsFeed', 'unfollow', 'getNewsFeed']
args = [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
expected = [None, None, [5], None, None, [6, 5], None, [5]]
```

### Case 2

```python
ops = ['Twitter', 'postTweet', 'postTweet', 'postTweet', 'getNewsFeed']
args = [[], [1, 1], [1, 2], [1, 3], [1]]
expected = [None, None, None, None, [3, 2, 1]]
```

### Case 3

```python
ops = ['Twitter', 'postTweet', 'postTweet', 'follow', 'getNewsFeed']
args = [[], [1, 10], [2, 20], [1, 2], [1]]
expected = [None, None, None, None, [20, 10]]
```

### Case 4

```python
ops = ['Twitter', 'follow', 'follow', 'postTweet', 'postTweet', 'getNewsFeed']
args = [[], [1, 2], [1, 3], [2, 100], [3, 200], [1]]
expected = [None, None, None, None, None, [200, 100]]
```

### Case 5

```python
ops = ['Twitter', 'postTweet', 'follow', 'getNewsFeed', 'unfollow', 'getNewsFeed']
args = [[], [2, 50], [1, 2], [1], [1, 2], [1]]
expected = [None, None, None, [50], None, []]
```

## Notes

- Brute-force approach:
- Optimized approach:
- Complexity:
- Edge cases and pitfalls:

## Run

```bash
python train.py run design-twitter
```
