from typing import List


def arrayPairSum(nums: List[int]) -> int:
    sort_n = sorted(nums)
    s = 0

    for i in range(0, len(nums), 2):
        print(i, sort_n[i], sort_n[i + 1])
        s += min([sort_n[i], sort_n[i + 1]])

    return s


print(arrayPairSum([1, 4, 3, 2]))
print(arrayPairSum([6, 2, 6, 5, 1, 2]))
