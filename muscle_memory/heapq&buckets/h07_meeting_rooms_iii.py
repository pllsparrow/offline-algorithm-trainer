# Input: room count and meeting count, then meetings with unique start times.
# Output: the room that hosted the most meetings; ties use the smaller room id.

import sys


def solve() -> None:
    room_count, meeting_count = map(int, sys.stdin.readline().split())
    meetings = [tuple(map(int, sys.stdin.readline().split())) for _ in range(meeting_count)]

    # Compute and print the room id.


if __name__ == "__main__":
    solve()
