import sys


def main() -> None:
    # Format: Input: arg1: edges2: count then values. Output: 1 if true else 0.
    data = sys.stdin.buffer.read().split()
    p = 0
    m_v0 = int(data[p]); p += 1
    v0 = [[int(data[p + w * i + j]) for j in range(2)] for i in range(m_v0)]; p += 2 * m_v0
    # TODO: compute the answer from v0 and print it


if __name__ == "__main__":
    main()
