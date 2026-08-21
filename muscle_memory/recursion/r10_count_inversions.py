# Input: n, followed by n integers.
# Output: the number of pairs i < j for which values[i] > values[j].

import sys


def solve() -> None:
    n = int(sys.stdin.readline())
    values = list(map(int, sys.stdin.readline().split())) if n else []

    # Count cross-half inversions while merging two sorted halves.


if __name__ == "__main__":
    solve()
