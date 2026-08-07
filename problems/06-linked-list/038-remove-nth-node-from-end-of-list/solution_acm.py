import sys


def main() -> None:
    # Format: Input: arg1: a linked list: count n then n integers; arg2: an integer. Output: the values space-separated.
    data = sys.stdin.buffer.read().split()
    p = 0
    n_v0 = int(data[p]); p += 1
    v0 = list(map(int, data[p:p + n_v0])); p += n_v0
    v1 = int(data[p]); p += 1
    # TODO: compute the answer from v0, v1 and print it


if __name__ == "__main__":
    main()
