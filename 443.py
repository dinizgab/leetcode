def compress(chars):
    counter = 1
    i = 0
    result = ""
    for j in range(1, len(chars) + 1):
        if j < len(chars) and chars[i] == chars[j]:
            counter += 1
        else:
            result += chars[i]
            if counter > 1:
                result += str(counter)
            counter = 1
            i = j
            j += 1

    length = len(result)
    for i in range(length):
        chars[i] = result[i]

    return length


print(compress(["a", "a", "b", "b", "c", "c"]))
