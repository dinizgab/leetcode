def is_palindrome(s):
    s = s.lower()

    i, j = 0, len(s) - 1
    while i < j:
        if not s[i].isalnum():
            i += 1
            continue

        if not s[j].isalnum():
            j -= 1
            continue

        if s[i] != s[j]:
            return False

        i += 1
        j -= 1

    return True


print(is_palindrome("tab a cat"))
print(is_palindrome("Was it a car or a cat I saw?"))
