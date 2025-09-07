from typing import List


def removeDuplicates(nums: List[int]) -> int:
    i = 0
    n = len(nums)
    reps = 1

    for j in range(1, n):
        if nums[i] == nums[j]:
            reps += 1

            if reps > 2:
                continue

    return i + 1


print(removeDuplicates([1, 1, 1, 2, 2, 3]))
print(removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))
