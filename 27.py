def removeElement(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] == val:

            for j in range(i, len(nums)):
                if nums[j] != val:
                    k += 1
                    nums[i], nums[j] = nums[j], nums[i]
                    break

    return len(nums) - k


def removeElementLinear(nums, val):
    k = len(nums) - 1
    for i in range(len(nums)):
        if nums[i] == val:
            nums[k], nums[i] = nums[i], nums[k]
            k -= 1

    return len(nums) - k


print(removeElementLinear([0,1,2,2,3,0,4,2], 2)) # 5
print(removeElement([3,2,2,3], 3)) # 2
