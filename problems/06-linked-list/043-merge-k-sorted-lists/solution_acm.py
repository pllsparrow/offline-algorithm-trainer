import sys


def main() -> None:
    # Format: Input: arg1: k linked lists: count k, then per list count n and n integers. Output: the values space-separated.
    data = sys.stdin.buffer.read().split()
    p = 0
    k_v0 = int(data[p]); p += 1
    v0 = []
    for _ in range(k_v0):
        n_v0 = int(data[p]); p += 1
        v0.append(list(map(int, data[p:p + n_v0]))); p += n_v0
    # TODO: compute the answer from v0 and print it


if __name__ == "__main__":
    main()
