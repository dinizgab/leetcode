from typing import List


def findDisappearedNumbers(nums: List[int]) -> List[int]:
    n = len(nums)
    count = [0] * n

    for i in range(n):
        count[nums[i] - 1] += 1

    res = []
    for i in range(len(count)):
        if count[i] == 0:
            res.append(i + 1)

    return res


def findDisappearedNumbersConstantMem(nums):
    res = []

    for i in range(len(nums)):
        while nums[i] != nums[nums[i] - 1]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

    for j in range(len(nums)):
        if nums[j] != j + 1:
            res.append(j + 1)

    return res


print(findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
print(findDisappearedNumbers([1, 1]))

print(findDisappearedNumbersConstantMem([4, 3, 2, 7, 8, 2, 3, 1]))
print(findDisappearedNumbersConstantMem([1, 1]))
