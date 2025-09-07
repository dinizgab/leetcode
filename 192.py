def isSubsequence(s: str, t: str) -> bool:
    i, j = 0, 0
    n, m = len(s), len(t)

    while j < m:
        if i < n and s[i] == t[j]:
            i += 1

        j += 1

    return i == n


s = "abc"
t = "ahbgdc"
print(isSubsequence(s, t))
