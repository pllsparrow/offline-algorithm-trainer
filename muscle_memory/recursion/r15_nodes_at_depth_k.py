# Input: n k, followed by n level-order tokens; the root has depth 0.
# Output: values at depth k from left to right on one line.

import sys


def solve() -> None:
    n, target_depth = map(int, sys.stdin.readline().split())
    nodes = sys.stdin.readline().split() if n else []

    # Carry the current depth downward and stop once the target is reached.


if __name__ == "__main__":
    solve()
