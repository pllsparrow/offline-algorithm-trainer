import sys


def main() -> None:
    # Format: Input: arg1: edges3: count then values; arg2: an integer list: count n then n integers. Output: 1 if true else 0.
    data = sys.stdin.buffer.read().split()
    p = 0
    m_v0 = int(data[p]); p += 1
    v0 = [[int(data[p + w * i + j]) for j in range(3)] for i in range(m_v0)]; p += 3 * m_v0
    n_v1 = int(data[p]); p += 1
    v1 = list(map(int, data[p:p + n_v1])); p += n_v1
    # TODO: compute the answer from v0, v1 and print it


if __name__ == "__main__":
    main()
