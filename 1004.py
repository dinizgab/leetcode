from typing import List


def longestOnes(nums: List[int], k: int) -> int:
    left, right = 0, 0
    max_sub = 0
    available_flips = k

    while right < len(nums):
        if nums[right] == 1:
            right += 1
        else:
            if available_flips > 0:
                available_flips -= 1
                right += 1
            else:
                max_sub = max(max_sub, right - left)
                while left < right and available_flips == 0:
                    if nums[left] == 0:
                        available_flips += 1

                    left += 1

    return max_sub


nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2

nums2 = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
k2 = 3

print(longestOnes(nums, k))
print(longestOnes(nums2, k2))
