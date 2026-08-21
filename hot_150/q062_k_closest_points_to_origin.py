# Input: points: edges2: count then values; k: an integer.
# Output: k points, one x y pair per line (any order).
import heapq


def kClosest():
    n = int(input())
    heap = []
    counts = 0
    points = []
    for _ in range(n):
        cur = list(map(int, input().split()))
        dis = cur[0] * cur[0] + cur[1] * cur[1]
        node = [-dis, cur[0], cur[1]]
        points.append(node)
        heapq.heappush(heap, node)
        counts += 1

    k = int(input())

    while counts > k:
        heapq.heappop(heap)
        counts -= 1

    while heap:
        res = heapq.heappop(heap)
        print(f"{res[1]} {res[2]}")

    return







    return

if __name__ == "__main__":
    kClosest()
