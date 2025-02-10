def largestAltitude(gain):
    # - We start at point 0
    # - We gain or loss altitude as we pass through the `gain` array
    # - Our altitude in point i should be the sum of the current point + before points
    # - (Basically a prefix sum)
    # - The result should be the max(0, max(prefix_array))

    # - This can be solved in O(n)
    prefix = []
    for i in range(0, len(gain)):
        if i == 0:
            prefix.append(gain[i])
        else:
            res = prefix[i - 1] + gain[i]
            prefix.append(res)

    largest = float('-inf')
    for j in range(0, len(gain)):
        if prefix[j] > largest:
            largest = prefix[j]

    return max(0, largest)


print(largestAltitude([-5, 1, 5, 0, -7]))
print(largestAltitude([-4, -3, -2, -1, 4, 3, 2]))
print(largestAltitude([-4, -5]))


# Each value of the array is the net gain of the altitude, meaning that, given this array: [-5, 1, 5, 0, -7]
# From the first point that the biker starts (altitude 0) to the first point of the array, the altitude lost was -5,
# to the second point he gained 1, so his relative altitude to 0 is now -4.

# Given that, the relative altitude of the biker is the prefix sum of the ith value, in this case, the result for each i value is:

# WE START AT 0 ALTITUDE
#  |
#  v
# [0, -5, -4, 1, 1, -6]

# Each next value is calculated based on the previous altitude
