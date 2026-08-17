# Input: n, k, and initial capital, then profits and required capitals.
# Output: the maximum capital after at most k projects.

import sys


def solve() -> None:
    n, k, capital = map(int, sys.stdin.readline().split())
    profits = list(map(int, sys.stdin.readline().split()))
    required = list(map(int, sys.stdin.readline().split()))

    # Compute and print the final capital.


if __name__ == "__main__":
    solve()
