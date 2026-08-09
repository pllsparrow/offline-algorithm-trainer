# Input: s: a string token; t: a string token.
# Output: 1 if true else 0.

import sys


def main() -> None:
    s = sys.stdin.readline().strip()
    t = sys.stdin.readline().strip()
    answer = 0

    if len(s) != len(t):
        sys.stdout.write(str(answer) + "\n")
        return

    counts = [0] * 26

    for i in range(len(s)):
        counts[ord(s[i]) - ord("a")] += 1
        counts[ord(t[i]) - ord("a")] -= 1

    if counts == [0] * 26:
        answer = 1

    sys.stdout.write(str(answer) + "\n")


if __name__ == "__main__":
    main()
