# Input: n, followed by a complete expression tree in level order.
# Output: its integer value; operators are +, -, and *.

import sys


def solve() -> None:
    n = int(sys.stdin.readline())
    tokens = sys.stdin.readline().split()

    # Evaluate both child expressions before applying the current operator.


if __name__ == "__main__":
    solve()
