from typing import List


def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    m = {}
    is_valid = False

    for i, n in enumerate(nums):
        if n in m:
            is_valid = abs(i - m[n]) <= k

        if is_valid:
            break

        m[n] = i

    return is_valid
