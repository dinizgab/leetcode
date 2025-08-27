def max_number_vowels(s, k):
    max_vowels = 0
    curr = 0
    for i in range(0, k):
        if s[i] in 'aeiou':
            curr += 1

    for i in range(len(s) - k):
        if s[i + k] in 'aeiou':
            curr += 1

        if s[i] in 'aeiou':
            curr -= 1

        max_vowels = max(max_vowels, curr)

    return max_vowels


print(max_number_vowels("bacacbefaobeacfe", 5))
