# Input: stones: an integer list: count n then n integers.
# Output: the integer.

import heapq


def lastStoneWeight() -> None:
    n = int(input())
    stones = list(map(int, input().split()))

    heap = [-stone for stone in stones]
    heapq.heapify(heap)

    while n > 1:
        y = -heapq.heappop(heap)
        x = -heapq.heappop(heap)
        n -= 2

        if x < y:
            cur = x - y
            heapq.heappush(heap, cur)
            n += 1

    if heap:
        print(-heap[0])
    else:
        print(0)

    return



if __name__ == "__main__":
    lastStoneWeight()
