def maxArea(height) -> int:
    biggest = float("-inf")

    i = 0
    j = len(height) - 1
    while i < j:
        area = (j - i) * min(height[j], height[i])
        if area > biggest:
            biggest = area

        if height[j] > height[i]:
            i += 1
        else:
            j -= 1

        # if height[i] < height[j]:
        #    i = j
        # j += 1
        # This code commented above is wrong, because it doesn't explore all the possibilities,
        # however, it passes in almost all test cases.
        #
        # To explore all the possibilities without having an inner loop, we need to explore from
        # the end and the beginning at the same time, and update the values based on the size of each one.
        #
        # However, my logic to calculate the biggest area is right

    return biggest


print(maxArea([1, 2, 1]))
