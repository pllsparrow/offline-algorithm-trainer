# Input: n, followed by n level-order 0/1 tokens; null marks a missing node.
# Output: the pruned token count and pruned level-order tokens.

import sys


def solve() -> None:
    n = int(sys.stdin.readline())
    nodes = sys.stdin.readline().split() if n else []

    # Decide whether to keep a node only after both children have been processed.


if __name__ == "__main__":
    solve()
