def pivotIndex(nums) -> int:
    n = len(nums)

    prefix = [0 for _ in range(len(nums))]
    prefix[0] = nums[0]
    for i in range(1, len(nums)):
        prefix[i] = prefix[i - 1] + nums[i]

    suffix = [0 for _ in range(len(nums))]
    suffix[n - 1] = nums[n - 1]
    for j in range(n - 2, -1, -1):
        suffix[j] = suffix[j + 1] + nums[j]

    for k in range(0, n):
        if prefix[k] == suffix[k]:
            return k

    return -1


print(pivotIndex([2, 1, -1]))
