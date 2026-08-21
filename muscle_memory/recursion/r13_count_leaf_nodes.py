# Input: n, followed by n level-order tokens; null marks a missing node.
# Output: the number of leaf nodes.

import sys


def solve() -> None:
    n = int(sys.stdin.readline())
    nodes = sys.stdin.readline().split() if n else []

    # A leaf contributes one; an internal node combines both subtree counts.


if __name__ == "__main__":
    solve()
