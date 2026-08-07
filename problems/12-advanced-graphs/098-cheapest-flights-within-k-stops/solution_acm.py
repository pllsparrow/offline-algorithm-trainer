import sys


def main() -> None:
    # Format: Input: arg1: an integer; arg2: edges3: count then values; arg3: an integer; arg4: an integer; arg5: an integer. Output: the integer.
    data = sys.stdin.buffer.read().split()
    p = 0
    v0 = int(data[p]); p += 1
    m_v1 = int(data[p]); p += 1
    v1 = [[int(data[p + w * i + j]) for j in range(3)] for i in range(m_v1)]; p += 3 * m_v1
    v2 = int(data[p]); p += 1
    v3 = int(data[p]); p += 1
    v4 = int(data[p]); p += 1
    # TODO: compute the answer from v0, v1, v2, v3, v4 and print it


if __name__ == "__main__":
    main()
