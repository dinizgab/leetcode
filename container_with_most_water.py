def maxArea(heights):
    i, j = 0, len(heights) - 1

    most_water = float('-inf')
    while i < j:
        h = min(heights[i], heights[j])
        b = j - i

        most_water = max(most_water, b * h)

        if heights[i] <= heights[j]:
            i += 1
        else:
            j -= 1

    return most_water


print(maxArea([1, 7, 2, 5, 4, 7, 3, 6]))
print(maxArea([2, 2, 2]))
