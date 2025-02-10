def searchInsert(nums, target):
    def binSearch(arr, v, left, right):
        if left > right:
            return left

        middle = (left + right) // 2
        if arr[middle] == v:
            return middle
        elif arr[middle] > v:
            return binSearch(arr, v, left, middle - 1)
        else:
            return binSearch(arr, v, left + 1, right)

    return binSearch(nums, target, 0, len(nums) - 1)


print(searchInsert([1, 3], 2))  # 2
print(searchInsert([1, 3, 5, 6], 2))  # 2
print(searchInsert([1, 3, 5, 6], 5))  # 2
print(searchInsert([1, 3, 5, 6], 7))  # 2
