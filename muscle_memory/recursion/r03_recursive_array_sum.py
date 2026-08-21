# Input: n, followed by n integers.
# Output: their sum; the sum of an empty array is 0.

import sys


def solve() -> None:
    n = int(sys.stdin.readline())
    values = list(map(int, sys.stdin.readline().split())) if n else []

    # Express the current answer using one element and a smaller suffix.


if __name__ == "__main__":
    solve()
