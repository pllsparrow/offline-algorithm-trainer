import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    height = data[1:1 + n]
    # TODO: compute and print the trapped volume


if __name__ == "__main__":
    main()
