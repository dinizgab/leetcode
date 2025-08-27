from collections import defaultdict


def topKFrequent(nums, k: int):
    count = defaultdict(int)
    group = [[] for i in range(len(nums) + 1)]

    for n in nums:
        count[n] += 1

    for n, freq in count.items():
        group[freq].append(n)

    res = []
    for i in range(len(group) - 1, 0, -1):
        for n in group[i]:
            res.append(n)
            if len(res) == k:
                return res


print(topKFrequent([1, 2, 2, 3, 3, 3, 3, 4], 2))
print(topKFrequent([1, 1, 1, 2, 2, 3], 2))
