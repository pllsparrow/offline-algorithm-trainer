# Input: n and m, then arr1 and a unique subset arr2.
# Output: arr1 in relative order, followed by remaining values ascending.

import sys


def solve() -> None:
    n, m = map(int, sys.stdin.readline().split())
    arr1 = list(map(int, sys.stdin.readline().split()))
    arr2 = list(map(int, sys.stdin.readline().split()))

    # Compute and print the reordered array.


if __name__ == "__main__":
    solve()
