def tupleSameProduct(nums):
    counter = {}
    res = 0

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            product = nums[i] * nums[j]
            res += counter.get(product, 0)
            counter[product] = counter.get(product, 0) + 1

    return res * 8


print(tupleSameProduct([2, 3, 4, 6]))
