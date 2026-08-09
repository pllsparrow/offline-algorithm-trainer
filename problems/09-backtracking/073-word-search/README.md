# 073. Word Search

- Chapter: 09. Backtracking
- Difficulty: Medium
- Source: https://leetcode.com/problems/word-search/
- Reference: https://neetcode.io/problems/search-for-word?list=neetcode150

## Goal

Classic interview problem for Word Search. Practice choice paths and pruning. Start with a brute-force idea, then optimize to an interview-ready complexity.

## Interview Focus

- Identify the core pattern: choice paths.
- Before coding, state the invariant or state definition: pruning.
- After it passes, explain the time complexity, space complexity, and one edge case.

## ACM Format

Input: board: a char board: rows r, cols c, then r lines of c chars; word: a string token. Output: 1 if true else 0.

## Local Examples

### Case 1

**Input**

```
3 4
A B C E
S F C S
A D E E
ABCCED
```

**Output**

```
1
```

### Case 2

**Input**

```
3 4
A B C E
S F C S
A D E E
SEE
```

**Output**

```
1
```

### Case 3

**Input**

```
3 4
A B C E
S F C S
A D E E
ABCB
```

**Output**

```
0
```

## Run

```bash
python3 train.py run word-search
```
