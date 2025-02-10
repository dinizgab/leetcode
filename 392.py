def isSubsequence(s, t):
    #  Given two strings, s and t
    #  Return true if s is a subsequence of t
    i = 0
    j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1

        j += 1

    return i == len(s)


print(isSubsequence("abc", "ahbgdc")) #  true
print(isSubsequence("abc", "ahgdc")) #  false 
print(isSubsequence("axc", "ahgdc")) #  false 
