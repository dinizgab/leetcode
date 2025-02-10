from collections import defaultdict


def good_pairs(nums):
    # nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
    # nums[i] - rev(nums[i]) == nums[j] - rev(nums[j])

    counter = defaultdict(int)
    pairs = 0

    for i in range(len(nums)):
        rev = int(str(nums[i])[::-1])

        diff = nums[i] - rev
        pairs += counter[diff]
        counter[diff] += 1

    return int(pairs % (10**9 + 7))


print(good_pairs([42, 11, 1, 97]))
