# Input: rows, cols, and k, then a matrix sorted by rows and columns.
# Output: the k-th smallest integer.

import sys


def solve() -> None:
    rows, cols, k = map(int, sys.stdin.readline().split())
    matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(rows)]

    # Compute and print the answer.


if __name__ == "__main__":
    solve()
