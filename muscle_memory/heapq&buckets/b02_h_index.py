# Input: n, then n non-negative citation counts.
# Output: the h-index.

import sys


def solve() -> None:
    n = int(sys.stdin.readline())
    citations = list(map(int, sys.stdin.readline().split()))

    # Compute and print the answer.


if __name__ == "__main__":
    solve()
