# Input: first line q (operations), then q lines of 'op args...'.
# Output: one result per operation (null for void; space-separated values for lists)

import heapq

class KthLargest:
    def __init__(self, k: int, nums: list[int]) -> None:
        self.k = k
        self.heap = nums.copy()

        heapq.heapify(self.heap)

        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]


def main() -> None:
    operation_count = int(input())
    results = []

    for _ in range(operation_count):
        parts = input().split()
        operation = parts[0]

        if operation == "KthLargest":
            k = int(parts[1])
            nums_count = int(parts[2])
            nums = list(map(int, parts[3 : 3 + nums_count]))

            kth_largest = KthLargest(k, nums)
            results.append("null")

        elif operation == "add":
            val = int(parts[1])
            result = kth_largest.add(val)
            results.append(str(result))

    print("\n".join(results))


if __name__ == "__main__":
    main()

