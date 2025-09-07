from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    comp = {}

    for i, n in enumerate(nums):
        c = target - n

        if c in comp:
            return [i, comp[c]]

        comp[c] = i
