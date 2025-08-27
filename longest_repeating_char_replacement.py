# This is wrong
def character_replacement(s, k):
    res = 0
    ignored = 0
    i = 0
    j = 0

    curr = 0
    while j < len(s):
        if s[i] == s[j]:
            curr += 1
            j += 1
        else:
            if ignored < k:
                ignored += 1
                j += 1
                curr += 1
            else:
                i = j
                ignored = 0
                curr = 0

        res = max(curr, res)

    return res


print(character_replacement("XYYX", 2))
print(character_replacement("AAABABB", 1))
print(character_replacement("ABAA", 0))
