# Input: n, followed by n level-order tokens; null marks a missing node.
# Output: the sum of leaves that are left children.

import sys


def solve() -> None:
    n = int(sys.stdin.readline())
    nodes = sys.stdin.readline().split() if n else []

    # Pass enough context to distinguish a left leaf from any other leaf.


if __name__ == "__main__":
    solve()
