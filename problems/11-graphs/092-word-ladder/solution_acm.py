import sys


def main() -> None:
    # Format: Input: arg1: a string token; arg2: a string token; arg3: a string list: count n then n tokens. Output: the integer.
    data = sys.stdin.buffer.read().split()
    p = 0
    v0 = data[p].decode(); p += 1
    v1 = data[p].decode(); p += 1
    n_v2 = int(data[p]); p += 1
    v2 = [data[p + j].decode() for j in range(n_v2)]; p += n_v2
    # TODO: compute the answer from v0, v1, v2 and print it


if __name__ == "__main__":
    main()
