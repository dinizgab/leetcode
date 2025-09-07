from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    groups = {}

    # [26] 0 -> a, 1 -> b, ..., 25 -> z

    for s in strs:
        counter = [0] * 26

        for c in s:
            i = ord(c) - 97
            counter[i] += 1

        if tuple(counter) in groups:
            groups[tuple(counter)].append(s)
        else:
            groups[tuple(counter)] = [s]

    return list(groups.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
