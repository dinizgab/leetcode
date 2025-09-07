from typing import List


def minSubArrayLen(target: int, nums: List[int]) -> int:
    i, j = 0, 0
    res = float("inf")
    tot = 0

    while j < len(nums):
        tot += nums[j]

        while tot >= target:
            res = min(res, j - i + 1)
            tot -= nums[i]
            i += 1

        j += 1

    return 0 if res == float("inf") else res


print(minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
print(minSubArrayLen(4, [1, 4, 4]))
print(minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))
