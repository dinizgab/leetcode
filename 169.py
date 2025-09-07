from collections import defaultdict
from typing import List


def majorityElement(nums: List[int]) -> int:
    counter = defaultdict(int)
    res = 0
    maj_count = float("-inf")

    for n in nums:
        counter[n] += 1

        if counter[n] > maj_count:
            maj_count = counter[n]
            res = n

    return res


def majorityElementO1(nums: List[int]) -> int:
    candidate = 0
    counter = 0

    for n in nums:
        if candidate == 0:
            candidate = n

        if candidate == n:
            counter += 1
        else:
            counter -= 1

    return candidate


print(majorityElement([3, 2, 3]))
print(majorityElement([2, 2, 1, 1, 1, 2, 2]))
