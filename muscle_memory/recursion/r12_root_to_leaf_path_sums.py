# Input: n, followed by n level-order tokens; null marks a missing node.
# Output: all root-to-leaf sums in non-decreasing order on one line.

import sys


def solve() -> None:
    n = int(sys.stdin.readline())
    nodes = sys.stdin.readline().split() if n else []

    # Carry the running sum downward and record it only at leaves.


if __name__ == "__main__":
    solve()
