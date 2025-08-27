def longestConsecutive(nums):
    nums = set(nums)

    longest = 0
    for n in nums:
        if (n - 1) not in nums:
            length = 1
            while n + length in nums:
                length += 1
            longest = max(longest, length)

    return longest


print(longestConsecutive([2, 20, 4, 10, 3, 4, 5]))
