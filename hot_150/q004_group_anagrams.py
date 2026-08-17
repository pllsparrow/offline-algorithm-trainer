# Input: strs: a string list: count n then n tokens.
# Output: each group on its own line (sorted; each group sorted).

import sys
from collections import defaultdict


def main() -> None:
    n = int(sys.stdin.readline())
    words = [
        sys.stdin.readline().rstrip("\n")
        for _ in range(n)
    ]


    seen = defaultdict(list)

    for word in words:
        str_sorted = "".join(sorted(word))
        seen[str_sorted].append(word)

    groups = [sorted(group) for group in seen.values()]
    groups.sort()
    for group in groups:
        print(" ".join(group))


if __name__ == "__main__":
    main()







