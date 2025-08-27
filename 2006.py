from collections import defaultdict


def count_k_difference_on2(nums, k):
    pairs = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i < j and abs(nums[i] - nums[j]) == k:
                pairs += 1

    return pairs


# [1, 2, 2, 1] 1
# loop through nums
# subtract nums[i] - k
# add nums[i] + k
# save these values in a counter dict -> dict[val] = val
# if nums[i] in dict -> pairs += 1
def count_k_difference_on(nums, k):
    pairs = 0
    counter = defaultdict(int)

    for i in range(len(nums)):
        sum = nums[i] + k
        sub = nums[i] - k

        pairs += counter[sum]
        pairs += counter[sub]

        counter[nums[i]] += 1

    return pairs


print(count_k_difference_on([1, 2, 2, 1], 1))
print(count_k_difference_on([1, 3], 3))
print(count_k_difference_on([3, 2, 1, 5, 4], 2))
