import sys


def main() -> None:
    # Format: Input: arg1: a binary tree: count n then n level-order values (null for missing); arg2: a binary tree: count n then n level-order values (null for missing). Output: 1 if true else 0.
    data = sys.stdin.buffer.read().split()
    p = 0
    n_v0 = int(data[p]); p += 1
    v0 = [None if data[p + i] == b'null' else int(data[p + i]) for i in range(n_v0)]; p += n_v0
    n_v1 = int(data[p]); p += 1
    v1 = [None if data[p + i] == b'null' else int(data[p + i]) for i in range(n_v1)]; p += n_v1
    # TODO: compute the answer from v0, v1 and print it


if __name__ == "__main__":
    main()
