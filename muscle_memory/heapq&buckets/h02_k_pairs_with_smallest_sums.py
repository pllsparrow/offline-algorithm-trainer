# Input: n, m, and k, then two ascending integer arrays.
# Output: k value pairs with the smallest sums; valid boundary ties are accepted.

import sys


def solve() -> None:
    n, m, k = map(int, sys.stdin.readline().split())
    nums1 = list(map(int, sys.stdin.readline().split()))
    nums2 = list(map(int, sys.stdin.readline().split()))

    # Print one selected pair per line.


if __name__ == "__main__":
    solve()
