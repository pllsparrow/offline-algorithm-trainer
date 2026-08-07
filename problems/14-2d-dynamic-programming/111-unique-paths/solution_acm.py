import sys


def main() -> None:
    # Format: Input: arg1: an integer; arg2: an integer. Output: the integer.
    data = sys.stdin.buffer.read().split()
    p = 0
    v0 = int(data[p]); p += 1
    v1 = int(data[p]); p += 1
    # TODO: compute the answer from v0, v1 and print it


if __name__ == "__main__":
    main()
