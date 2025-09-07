def wordPattern(pattern: str, s: str) -> bool:
    s = s.split()
    if len(s) != len(pattern):
        return False

    c_to_w = {}
    w_to_c = {}
    for i in range(len(s)):
        c = pattern[i]
        w = s[i]

        if c in c_to_w and c_to_w[c] != w or w in w_to_c and w_to_c[w] != c:
            return False

        c_to_w[c] = w
        w_to_c[w] = c

    return True


pattern = "abba"
s = "dog cat cat dog"
print(wordPattern(pattern, s))

pattern = "abba"
s = "dog cat cat fish"
print(wordPattern(pattern, s))

pattern = "aaaa"
s = "dog cat cat dog"
print(wordPattern(pattern, s))

pattern = "abba"
s = "dog dog dog dog"
print(wordPattern(pattern, s))
