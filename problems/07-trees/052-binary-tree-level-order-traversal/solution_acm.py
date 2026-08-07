import sys
from collections import deque


def main() -> None:
    tokens = sys.stdin.buffer.read().split()
    n = int(tokens[0])
    values = [None if token == b"null" else int(token) for token in tokens[1:1 + n]]
    # TODO: print one space-separated level per line


if __name__ == "__main__":
    main()
