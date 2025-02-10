def reverseVowels(s: str) -> str:
    vowels = ['a', 'e', 'i', 'o', 'u']
    stringVowels = []
    for i in range(0, len(s)):
        if s[i].lower() in vowels:
            stringVowels.append(s[i])
    
    print(stringVowels)
    result = ""
    for i in range(0, len(s)):
        if s[i].lower() in vowels:
            result += stringVowels.pop()
            print(result)
        else:
            result += s[i]

    return s

print(reverseVowels("IceCreAm"))
