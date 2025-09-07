def romanToInt(s: str) -> int:
    r_to_i = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    total = 0

    for i, n in enumerate(s):
        curr = r_to_i[n]
        next = r_to_i[s[i - 1]] if i > 0 else 0

        if curr < next:
            total -= curr
        else:
            total += curr

    return total
