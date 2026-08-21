# Input: n >= 1, followed by n integers.
# Output: the maximum integer.

import sys


def solve() -> None:
    n = int(sys.stdin.readline())
    values = list(map(int, sys.stdin.readline().split()))

    # Compare the current element with the answer for a smaller suffix.


if __name__ == "__main__":
    solve()
