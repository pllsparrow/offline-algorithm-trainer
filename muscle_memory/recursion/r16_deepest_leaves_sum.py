# Input: n, followed by n level-order tokens; null marks a missing node.
# Output: the sum of all deepest leaf values.

import sys


def solve() -> None:
    n = int(sys.stdin.readline())
    nodes = sys.stdin.readline().split() if n else []

    # Return both the deepest relative depth and its sum from each subtree.


if __name__ == "__main__":
    solve()
