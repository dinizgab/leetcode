from typing import List


def summaryRanges(nums: List[int]) -> List[str]:
    start = 0
    sets = []

    if len(nums) == 0:
        return sets

    for i in range(1, len(nums)):
        curr = nums[i]
        prev = nums[i - 1]

        print(curr, prev)

        if curr != prev + 1:
            sets.append(
                f"{nums[start]}"
                if start == i - 1 else f"{nums[start]}->{prev}"
            )

            start = i

    sets.append(
        f"{nums[start]}"
        if start == len(nums) - 1 else f"{nums[start]}->{nums[-1]}"
    )

    return sets


print(summaryRanges([0, 1, 2, 4, 5, 7]))
print(summaryRanges([0, 2, 3, 4, 6, 8, 9]))
