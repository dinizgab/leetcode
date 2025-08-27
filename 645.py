from collections import defaultdict
from typing import List


def findErrorNums(nums: List[int]) -> List[int]:
    res = []
    seen = defaultdict(int)

    for n in nums:
        seen[n] += 1
        if seen[n] == 2:
            res.append(n)
            break

    for i in range(1, len(nums) + 1):
        if seen[i] == 0:
            res.append(i)
            break

    return res
