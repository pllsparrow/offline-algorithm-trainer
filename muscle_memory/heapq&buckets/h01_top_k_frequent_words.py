# Input: n, then n word lines, then k.
# Output: k words, ordered by frequency descending and word ascending.

import sys


def solve() -> None:
    n = int(sys.stdin.readline())
    words = [sys.stdin.readline().rstrip("\n") for _ in range(n)]
    k = int(sys.stdin.readline())

    # Print one selected word per line.


if __name__ == "__main__":
    solve()
