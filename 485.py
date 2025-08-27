def findMaxConsecutiveOnes(nums) -> int:
    count, max_count = 0, 0

    for n in nums:
        if n == 0:
            count = 0
        else:
            count += 1

        if count > max_count:
            max_count = count

    return max_count


print(findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
print(findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]))
print(findMaxConsecutiveOnes([0]))
