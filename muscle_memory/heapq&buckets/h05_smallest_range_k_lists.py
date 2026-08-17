# Input: k, then each sorted list as a length line followed by one values line.
# Output: the smallest inclusive range as two integers; ties use the smaller left bound.

import sys


def solve() -> None:
    list_count = int(sys.stdin.readline())
    lists = []
    for _ in range(list_count):
        length = int(sys.stdin.readline())
        values = list(map(int, sys.stdin.readline().split()))
        lists.append(values[:length])

    # Compute and print the left and right bounds.


if __name__ == "__main__":
    solve()
