#  This solution is O(n2), if k == len(nums),
#  so, for largest datasets, this is not optimal
def findMaxAverage(nums, k: int) -> float:
    largest_average = float("-inf")

    for i in range(len(nums)):
        average = 0
        if i + k > len(nums):
            break

        for j in range(i, i + k):
            print("j ", j)
            average += nums[j]

        print("average: ", average)

        average = average / k
        if average > largest_average:
            largest_average = average

    return largest_average


#  This one is O(n), we pre-calculate the first sum
#  and then calculate the next ones based on this first.
#  Just removing the leftmost number and adding the rightmost
def findMaxAverage2(nums, k):
    largest_average = float("-inf")
    curr_sum = 0

    for i in range(k):
        curr_sum += nums[i]
        largest_average = curr_sum / k

    for i in range(1, len(nums)):
        print(i, i + k)
        if i + k > len(nums):
            break
        curr_sum = curr_sum - nums[i - 1] + nums[i + k - 1]

        average = curr_sum / k
        if average > largest_average:
            largest_average = average

    return largest_average


print(findMaxAverage([1, 12, -5, -6, 50, 3], 4))
print(findMaxAverage2([1, 12, -5, -6, 50, 3], 4))
