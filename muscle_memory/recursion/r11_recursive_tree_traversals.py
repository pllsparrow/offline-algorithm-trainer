# Input: n, followed by n level-order tokens; null marks a missing node.
# Output: preorder, inorder, and postorder traversals on three lines.

import sys


def solve() -> None:
    n = int(sys.stdin.readline())
    nodes = sys.stdin.readline().split() if n else []

    # Change only when the current node is recorded around the two recursive calls.


if __name__ == "__main__":
    solve()
