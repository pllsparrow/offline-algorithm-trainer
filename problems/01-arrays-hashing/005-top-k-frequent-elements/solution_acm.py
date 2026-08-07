import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, k = data[0], data[1]
    nums = data[2:2 + n]
    # TODO: count frequencies, select k values, and print them sorted


if __name__ == "__main__":
    main()
