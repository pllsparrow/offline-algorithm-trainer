# Input: n, followed by n integers.
# Output: the integers in non-decreasing order.

import sys


def solve() -> None:
    n = int(sys.stdin.readline())
    values = list(map(int, sys.stdin.readline().split())) if n else []

    # Recursively sort both halves and merge their returned results.


if __name__ == "__main__":
    solve()
