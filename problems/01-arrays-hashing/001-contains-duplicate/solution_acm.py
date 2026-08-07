import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    nums = data[1:1 + n]
    # TODO: print 1 or 0


if __name__ == "__main__":
    main()
