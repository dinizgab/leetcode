from typing import List
from collections import defaultdict


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    seen = defaultdict(int)
    res = []

    for n in nums1:
        seen[n] += 1

    for n in nums2:
        if seen[n] > 0:
            res.append(n)
            seen[n] -= 1

    return res


nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]

print(intersect(nums1, nums2))
