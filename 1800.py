def max_ascending_sum(arr):
    max_sum = float('-inf')

    for i in range(len(arr)):
        j = i + 1
        count = arr[i]

        while j < len(arr) and arr[i] < arr[j]:
            count += arr[j]
            i = j
            j += 1

        if count > max_sum:
            max_sum = count

    return max_sum


print(max_ascending_sum([10, 20, 30, 5, 10, 50]))
print(max_ascending_sum([10, 20, 30, 40, 50]))
print(max_ascending_sum([12, 17, 15, 13, 10, 11, 12]))
