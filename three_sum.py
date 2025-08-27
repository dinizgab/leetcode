def threeSum(nums):
    nums = sorted(nums)
    res = []
    for i in range(len(nums)):
        if nums[i] > 0:
            break

        if i > 0 and nums[i] == nums[i - 1]:
            continue

        j, k = i + 1, len(nums) - 1

        while j < k and k < len(nums):
            total = nums[i] + nums[j] + nums[k]
            if total < 0:
                j += 1
            elif total > 0:
                k -= 1
            else:
                res.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
                while nums[j] == nums[j - 1] and j < k:
                    j += 1

    return res


print(threeSum([-1, 0, 1, 2, -1, -4]))
print(threeSum([0, 1, 1]))
print(threeSum([0, 0, 0]))
print(threeSum([0, 0, 0, 0]))
