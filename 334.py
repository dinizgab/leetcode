def increasingTriplet(nums) -> bool:
    i = 0
    j = 1
    result_i = -1
    result_j = -1
    result_k = -1

    while j < len(nums):
        if nums[i] < nums[j] or nums[result_i] > nums[j]:
            if result_i != -1 and result_j != -1 and nums[i] < nums[j]:
                result_k = j
            else:
                result_i = i
                result_j = j
            i = j

        j += 1

    print(result_i, result_j, result_k)
    return result_i != -1 and result_j != -1 and result_k != -1


print(increasingTriplet([20, 100, 10, 12, 5, 13]))
print(increasingTriplet([1, 2, 3, 4, 5]))
print(increasingTriplet([2, 1, 5, 0, 4, 6]))
print(increasingTriplet([5, 4, 3, 2, 1]))
print(increasingTriplet([0, 4, 2, 1, 0, -1, -3]))
print(increasingTriplet([1, 6, 2, 5, 1]))
