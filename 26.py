from typing import List


def removeDuplicates(nums: List[int]) -> int:
    i, j = 0, 1

    while j < len(nums):
        if nums[i] == nums[j]:
            j += 1
            continue

        i += 1
        nums[i] = nums[j]
        j += 1

    return i + 1


nums = [1, 1, 2]
nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(removeDuplicates(nums))
print(removeDuplicates(nums2))
