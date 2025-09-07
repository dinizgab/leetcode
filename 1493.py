from typing import List


def longestSubarray(nums: List[int]) -> int:
    deletions = 1
    i, j = 0, 0
    max_sub = 0

    while j < len(nums):
        if nums[j] == 1:
            j += 1
        else:
            if deletions == 0:
                while deletions == 0:
                    if nums[i] == 0:
                        deletions += 1

                    i += 1
            else:
                deletions -= 1
                j += 1

        max_sub = max(max_sub, j - i - 1)

    return max_sub


nums = [1, 1, 0, 1]
nums2 = [0, 1, 1, 1, 0, 1, 1, 0, 1]
nums3 = [1, 1, 1]

print(longestSubarray(nums))
print(longestSubarray(nums2))
print(longestSubarray(nums3))
