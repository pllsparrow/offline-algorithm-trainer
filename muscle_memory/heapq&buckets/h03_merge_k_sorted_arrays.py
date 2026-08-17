# Input: k, then each array as a length line followed by one values line.
# Output: all values in ascending order on one line.

import sys


def solve() -> None:
    array_count = int(sys.stdin.readline())
    arrays = []
    for _ in range(array_count):
        length = int(sys.stdin.readline())
        values = list(map(int, sys.stdin.readline().split()))
        arrays.append(values[:length])

    # Compute and print the merged values.


if __name__ == "__main__":
    solve()
