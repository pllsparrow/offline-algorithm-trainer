# Input: tasks: a string list: count n then n tokens; n: an integer.
# Output: the integer.
import sys
from typing import Counter

def taskScheduler():
    l = int(input())
    if l == 0:
        print(0)
        return

    tasks = []
    for _ in range(l):
        tasks.append(input())

    n = int(input())
    counts = Counter(tasks)

    f = max(counts.values())
    m = sum( freq == f for freq in counts.values())

    frame_length = (f - 1) * (n + 1) + m

    ans = max( l, frame_length)
    print(ans)

    return


if __name__ == "__main__":
    taskScheduler()
