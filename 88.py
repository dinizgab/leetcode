from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    midx, nidx, right = m - 1, n - 1, m + n - 1

    while nidx >= 0:
        if midx >= 0 and nums1[midx] > nums2[nidx]:
            nums1[right] = nums1[midx]
            midx -= 1
        else:
            nums1[right] = nums2[nidx]
            nidx -= 1

        right -= 1


nums1 = [4, 5, 6, 0, 0, 0]
nums2 = [1, 2, 3]
n = len(nums2)
m = len(nums1) - n

print(nums1, nums2, n, m)

merge(nums1, m, nums2, n)

print(nums1)
