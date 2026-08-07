import sys


def main() -> None:
    # Format: Input: arg1: string pairs: count m then m lines of two tokens. Output: the strings space-separated.
    data = sys.stdin.buffer.read().split()
    p = 0
    m_v0 = int(data[p]); p += 1
    v0 = [[data[p + 2 * i].decode(), data[p + 2 * i + 1].decode()] for i in range(m_v0)]; p += 2 * m_v0
    # TODO: compute the answer from v0 and print it


if __name__ == "__main__":
    main()
