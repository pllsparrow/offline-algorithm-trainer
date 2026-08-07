import sys


def main() -> None:
    # Format: Input: arg1: a random list: count n, then n lines of value and random-index (-1 for null). Output: count n then n lines of value and random-index (-1 for null).
    data = sys.stdin.buffer.read().split()
    p = 0
    n_v0 = int(data[p]); p += 1
    v0 = []
    for _ in range(n_v0):
        val = int(data[p]); idx = int(data[p + 1]); p += 2
        v0.append([val, None if idx == -1 else idx])
    # TODO: compute the answer from v0 and print it


if __name__ == "__main__":
    main()
