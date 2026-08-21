# Input: n, followed by n level-order tokens; null marks a missing node.
# Output: the sum of every node's absolute left/right subtree-sum difference.

import sys


def solve() -> None:
    n = int(sys.stdin.readline())
    nodes = sys.stdin.readline().split() if n else []

    # Return each subtree sum while accumulating the tilt as a side result.


if __name__ == "__main__":
    solve()
