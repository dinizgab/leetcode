from collections import defaultdict


def different_binary_string(nums):
    n = len(nums)
    seen = defaultdict(bool)

    for num in nums:
        seen[num] = True

    for i in range(2**n):
        b = f"{i:0{n}b}"

        if not seen[b]:
            return b


print(different_binary_string(['01', '10']))
print(different_binary_string(['00', '10']))
