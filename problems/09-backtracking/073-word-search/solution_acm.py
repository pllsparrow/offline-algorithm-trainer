import sys


def main() -> None:
    # Format: Input: arg1: a char board: rows r, cols c, then r lines of c chars; arg2: a string token. Output: 1 if true else 0.
    data = sys.stdin.buffer.read().split()
    p = 0
    r_v0 = int(data[p]); c_v0 = int(data[p + 1]); p += 2
    v0 = [[data[p + i * c_v0 + j].decode() for j in range(c_v0)] for i in range(r_v0)]; p += r_v0 * c_v0
    v1 = data[p].decode(); p += 1
    # TODO: compute the answer from v0, v1 and print it


if __name__ == "__main__":
    main()
