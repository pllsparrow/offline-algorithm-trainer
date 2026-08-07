import sys


def main() -> None:
    # Format: Input: arg1: a graph: count n, then per node degree d and d neighbour ids. Output: count n then n neighbour lists (degree then ids).
    data = sys.stdin.buffer.read().split()
    p = 0
    n_v0 = int(data[p]); p += 1
    v0 = []
    for _ in range(n_v0):
        d_v0 = int(data[p]); p += 1
        v0.append(list(map(int, data[p:p + d_v0]))); p += d_v0
    # TODO: compute the answer from v0 and print it


if __name__ == "__main__":
    main()
