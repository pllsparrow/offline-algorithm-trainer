import sys


def main() -> None:
    # Format: Input: arg1: an integer matrix: rows r, cols c, then r lines of c integers. Output: the integer.
    data = sys.stdin.buffer.read().split()
    p = 0
    r_v0 = int(data[p]); c_v0 = int(data[p + 1]); p += 2
    v0 = [list(map(int, data[p + i * c_v0:p + (i + 1) * c_v0])) for i in range(r_v0)]; p += r_v0 * c_v0
    # TODO: compute the answer from v0 and print it


if __name__ == "__main__":
    main()
