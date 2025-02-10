def clear_digits(s):
    counter = []

    for i in range(len(s)):
        if s[i].isalpha():
            counter.append(s[i])
        else:
            counter.pop()

    return ''.join(counter)


print(clear_digits("abc"))
print(clear_digits("c3"))
print(clear_digits("ac34"))
print(clear_digits("aca34"))
