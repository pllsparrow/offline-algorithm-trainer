# Input: nums: an integer list: count n then n integers; k: an integer.
# Output: the integer.
import sys
import heapq

def KthLargest():
    n = int(input())

    nums = list(map(int, input().split()))
    k = int(input())

    heap = []
    counts = 0

    for num in nums:
        heapq.heappush(heap, num)
        counts += 1

        while counts > k:
            heapq.heappop(heap)
            counts -= 1

    print(heapq.heappop(heap))

    return


if __name__ == "__main__":
    KthLargest()
