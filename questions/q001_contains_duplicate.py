# Input: nums: an integer list: count n then n integers.
# Output: 1 if true else 0.

import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()

    n = int(data[0])
    nums = list(map(int, data[1:n + 1]))

    seen = set()
    answer = 0

    for num in nums:
        if num in seen:
            answer = 1
            break
        seen.add(num)

    sys.stdout.write(str(answer) + "\n")

if __name__ == "__main__":
    main()
