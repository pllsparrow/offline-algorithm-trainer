# Input: n, followed by n level-order digit tokens; null marks a missing node.
# Output: the sum of the decimal numbers represented by all root-to-leaf paths.

import sys


def solve() -> None:
    n = int(sys.stdin.readline())
    nodes = sys.stdin.readline().split() if n else []

    # Extend the path number with current * 10 + digit.


if __name__ == "__main__":
    solve()
