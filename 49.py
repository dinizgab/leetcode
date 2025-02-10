def group_anagrams(strs):
    res = {}

    for w in strs:
        counter = [0 for i in range(26)]

        for letter in w:
            counter[ord(letter) - 97] += 1

        counter = list(map(str, counter))

        if '#'.join(counter) in res.keys():
            res['#'.join(counter)].append(w)
        else:
            res['#'.join(counter)] = [w]

    return [*res.values()]


print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(group_anagrams([""]))
print(group_anagrams(["a"]))
print(group_anagrams(["bdddddddddd", "bbbbbbbbbbc"]))
