from typing import List


def longestConsecutive(nums: List[int]) -> int:
    nums = set(nums)
    max_length = 0

    for n in nums:
        # if current number is the start of a sequence
        if n - 1 not in nums:
            length = 1
            while n + length in nums:
                length += 1

            max_length = max(max_length, length)

    return max_length


print(longestConsecutive([100, 4, 200, 1, 3, 2]))
