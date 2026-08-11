# Input: nums: an integer list: count n then n integers; target: an integer.
# Output: the values space-separated.


import sys
from typing import List


def main() -> None:
    n = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    target = int(sys.stdin.readline())

    seen = {}

    for i in range(n):
        cur_val = nums[i]
        need = target - cur_val

        if need in seen:
            sys.stdout.write(f"{seen[need]} {i}\n")
            return

        seen[cur_val] = i


if __name__ == "__main__":
    main()







