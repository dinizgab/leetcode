from typing import List
from collections import defaultdict


def findShortestSubArray(nums: List[int]) -> int:
    counter = defaultdict(int)
    first, last = {}, {}

    for i, n in enumerate(nums):
        counter[n] += 1

        if n not in first:
            first[n] = i
        last[n] = i

    degree = float('-inf')
    for v in counter.values():
        if v > degree:
            degree = v

    best = len(nums)
    for k, v in counter.items():
        if v == degree:
            best = min(best, last[k] - first[k] + 1)

    return best


print(findShortestSubArray([2, 2, 3, 1, 4, 2]))
print(findShortestSubArray([1, 2, 2, 3, 1]))
