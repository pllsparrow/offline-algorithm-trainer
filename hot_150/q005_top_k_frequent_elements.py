# Input: nums: an integer list: count n then n integers; k: an integer.
# Output: the values space-separated in ascending order.

from collections import Counter
import heapq
import sys


def solve() -> None:
    n = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    k = int(sys.stdin.readline())

    count = Counter(nums)

    ans = heapq.nlargest(k, count.keys(), key=count.get)

    print(*sorted(ans))




if __name__ == "__main__":
    solve()