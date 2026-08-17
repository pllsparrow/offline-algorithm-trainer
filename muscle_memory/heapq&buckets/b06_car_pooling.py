# Input: capacity and trip count, then passenger, start, and end for each trip.
# Output: 1 when all trips are feasible, otherwise 0.

import sys


def solve() -> None:
    capacity, trip_count = map(int, sys.stdin.readline().split())
    trips = [tuple(map(int, sys.stdin.readline().split())) for _ in range(trip_count)]

    # Compute and print 1 or 0.


if __name__ == "__main__":
    solve()
