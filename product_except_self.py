def productExceptSelf(nums):
    res = [1] * len(nums)

    prefix = 1
    for i in range(1, len(nums)):
        res[i] *= prefix
        prefix *= nums[i]

    postfix = 1
    for j in range(len(nums) - 1, -1, -1):
        res[j] *= postfix
        postfix *= nums[j]

    return res


print(productExceptSelf([1, 2, 4, 6]))
print(productExceptSelf([-1, 0, 1, 2, 3]))
