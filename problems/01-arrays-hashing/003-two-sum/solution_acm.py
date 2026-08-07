import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, target = data[0], data[1]
    nums = data[2:2 + n]
    # TODO: print the two zero-based indices


if __name__ == "__main__":
    main()
