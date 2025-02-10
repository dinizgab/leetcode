from collections import defaultdict


def good_pairs(nums):
    # i - nums[i] != j - nums[j]
    counter = defaultdict(int)
    good_pairs = 0
    total_pairs = (len(nums) * (len(nums) - 1)) / 2

    for i in range(len(nums)):
        diff = i - nums[i]
        good_pairs += counter[diff]
        counter[diff] += 1

    return int(total_pairs - good_pairs)


print(good_pairs([4, 1, 3, 3]))
