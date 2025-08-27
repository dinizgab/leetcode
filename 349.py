from typing import List


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    seen = set(nums1)
    res = set()

    for n in nums2:
        if n in seen:
            res.append(n)

    return res
