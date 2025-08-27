def two_sum(numbers, target):
    i, j = 0, len(numbers) - 1

    while i < j:
        a = numbers[i]
        b = numbers[j]

        if a + b > target:
            j -= 1
        elif a + b < target:
            i += 1
        else:
            return [i + 1, j + 1]


print(two_sum([1, 2, 3, 4], 3))
