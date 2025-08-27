def groupAnagrams(strs):
    group = {}

    for s in strs:
        s_code = [0] * 26
        for c in s:
            s_code[ord(c) - ord("a")] += 1

        group[tuple(s_code)].append(s)

    return list(group.values())


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"]))
