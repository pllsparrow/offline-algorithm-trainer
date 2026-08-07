import sys


def main() -> None:
    # Format: Input: arg1: a string token; arg2: a string token. Output: the string.
    data = sys.stdin.buffer.read().split()
    p = 0
    v0 = data[p].decode(); p += 1
    v1 = data[p].decode(); p += 1
    # TODO: compute the answer from v0, v1 and print it


if __name__ == "__main__":
    main()
