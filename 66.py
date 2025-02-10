# GAMBIARRA VERSION
def plusOne(digits):
    # The goal is to add 1 to the last element of the list
    # where each index represents a digit from the number

    # we can sum 1 at the last index, get its module by 10
    # insert in that index, and sum 1 on the second by last, get its module
    # and repeat over and over until i == 0
    i = len(digits) - 1
    carry = True
    res = []
    while i >= 0:
        if digits[i] == 9 and carry:
            res.insert(0, 0)
            carry = True
        else:
            curr = digits[i]
            if carry:
                curr += 1

            print(curr, carry, i)

            res.insert(0, curr)
            carry = False

        i -= 1

    if carry:
        res.insert(0, 1)

    return res


def plusOneCleanerVersion(digits):
    i = len(digits) - 1
    while i >= 0:
        print(digits[i])
        if digits[i] + 1 != 10:
            digits[i] += 1
            return digits

        digits[i] = 0
        if i == 0:
            return [1] + digits
        i -= 1


print(plusOneCleanerVersion([1, 2, 3]))
print(plusOneCleanerVersion([9, 9]))
# print(plusOne([1, 9, 9]))
# print(plusOne([1, 9]))
# print(plusOne([9, 9]))
# print(plusOne([9, 9, 9, 9, 9]))
# print(plusOne([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))
