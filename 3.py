def lengthOfLongestSubstring(s: str) -> int:
    seen = set()

    i, j = 0, 0
    m_s = 0

    while j < len(s):
        while s[j] in seen:
            seen.remove(s[i])
            i += 1

        seen.add(s[j])
        m_s = max(j - i + 1, m_s)
        j += 1

    return m_s


print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))
