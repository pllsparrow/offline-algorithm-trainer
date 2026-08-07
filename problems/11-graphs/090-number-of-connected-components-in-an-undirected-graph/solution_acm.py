import sys


def main() -> None:
    # Format: Input: arg1: an integer; arg2: edges2: count then values. Output: the integer.
    data = sys.stdin.buffer.read().split()
    p = 0
    v0 = int(data[p]); p += 1
    m_v1 = int(data[p]); p += 1
    v1 = [[int(data[p + w * i + j]) for j in range(2)] for i in range(m_v1)]; p += 2 * m_v1
    # TODO: compute the answer from v0, v1 and print it


if __name__ == "__main__":
    main()
