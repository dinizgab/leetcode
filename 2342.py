from collections import defaultdict


def sum_digits(num):
    total = 0

    while num > 0:
        total += num % 10
        num = num // 10

    return total


def maximum_sum(arr):
    counter = defaultdict(list)

    for num in arr:
        digit_sum = sum_digits(num)

        counter[digit_sum].append(num)

    max_sum = -1
    for k in counter.keys():
        bucket = counter[k]
        bucket.sort()

        if len(bucket) < 2:
            continue

        curr_sum = bucket[-1] + bucket[-2]
        if curr_sum > max_sum:
            max_sum = curr_sum

    return max_sum


print(sum_digits(10))
print(sum_digits(5))
print(sum_digits(123))

print(maximum_sum([18, 43, 36, 13, 7]))
