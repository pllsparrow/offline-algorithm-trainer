import sys


def main() -> None:
    # Format: Input: arg1: an integer. Output: the solution count S, then S boards each as n lines of Q/..
    data = sys.stdin.buffer.read().split()
    p = 0
    v0 = int(data[p]); p += 1
    # TODO: compute the answer from v0 and print it


if __name__ == "__main__":
    main()
