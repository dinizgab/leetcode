from typing import List
from collections import defaultdict


def maxOperations(nums: List[int], k: int) -> int:
    pairs = defaultdict(int)
    total = 0

    for n in nums:
        comp = k - n

        if n in pairs and pairs[n] > 0:
            total += 1
            pairs[n] -= 1
            pairs[comp] -= 1

        pairs[comp] += 1

    return total


nums = [1, 2, 3, 4]
k = 5
nums2 = [3, 1, 3, 4, 3]
k2 = 6
nums3 = [2, 3, 2, 3, 3]
k3 = 5
print(maxOperations(nums, k))
print(maxOperations(nums2, k2))
print(maxOperations(nums3, k3))
