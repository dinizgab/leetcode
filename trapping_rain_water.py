def trap(height):
    # Calculate max prefix array
    # Calculate max sufix array

    # Max prefix and max suffix arrays are arrays that stores the max values
    # previous to index i and after index i respectively

    # Current position total water is:
    # water_curr = min(prefix[i], sufix[i]) - height[i]
    n = len(height)

    prefix = [0] * n
    prefix[0] = height[0]
    for i in range(1, n):
        prefix[i] = max(height[i], prefix[i - 1])

    suffix = [0] * n
    suffix[-1] = height[-1]
    for i in range(n - 2, -1, -1):
        suffix[i] = max(height[i], suffix[i + 1])

    max_water = 0
    for i in range(0, n):
        max_water += min(prefix[i], suffix[i]) - height[i]

    return max_water


print(trap([0, 2, 0, 3, 1, 0, 1, 3, 2, 1]))
