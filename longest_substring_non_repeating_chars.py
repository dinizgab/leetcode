def len_longest_substring(s):
    max_str = 0
    i = 0
    j = 0
    seen = {}

    while j < len(s):
        # Updates i to the last apparition of s[j]
        if s[j] in seen:
            i = max(seen[s[j]] + 1, i)

        # Updates the map to the las apparition of s[j]
        seen[s[j]] = j

        # The max substring must be the difference between j and i
        # or the current one if it is already bigger
        max_str = max(max_str, j - i + 1)
        j += 1

    return max_str


print((len_longest_substring("zxyzxyz")))
print((len_longest_substring("zxyabcz")))
print((len_longest_substring("xxxx")))
print((len_longest_substring("pwwkew")))
