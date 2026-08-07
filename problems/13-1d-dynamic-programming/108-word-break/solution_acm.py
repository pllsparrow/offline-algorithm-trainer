import sys


def main() -> None:
    # Format: Input: arg1: a string token; arg2: a string list: count n then n tokens. Output: 1 if true else 0.
    data = sys.stdin.buffer.read().split()
    p = 0
    v0 = data[p].decode(); p += 1
    n_v1 = int(data[p]); p += 1
    v1 = [data[p + j].decode() for j in range(n_v1)]; p += n_v1
    # TODO: compute the answer from v0, v1 and print it


if __name__ == "__main__":
    main()
