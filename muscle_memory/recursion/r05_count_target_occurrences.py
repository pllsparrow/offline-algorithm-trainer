# Input: n target, followed by n integers.
# Output: the number of occurrences of target.

import sys


def solve() -> None:
    n, target = map(int, sys.stdin.readline().split())
    values = list(map(int, sys.stdin.readline().split())) if n else []

    # Let each recursive level contribute either zero or one.


if __name__ == "__main__":
    solve()
