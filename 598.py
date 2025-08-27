from typing import List
from collections import defaultdict


def maxCount(m: int, n: int, ops: List[List[int]]) -> int:
    matrix = [[0] * n for _ in range(m)]
    counter = defaultdict(int)

    for o in ops:
        x, y = o

        for i in range(x):
            for j in range(y):
                if i < x and j < y:
                    matrix[i][j] += 1

    max_idx = float('-inf')
    for i in range(m):
        for j in range(n):
            counter[matrix[i][j]] += 1
            if matrix[i][j] > max_idx:
                max_idx = matrix[i][j]

    return counter[max_idx]


# We don't need to compute all the number in the matrix like did above
# the solution will always be the smallest area affected by all the
# ops, they will always be a rectangle, starting from i = 0 and j = 0
# so, the smallest area of them will always be affected by the biggest one
def maxCountNoBruteForce(m: int, n: int, ops: List[List[int]]) -> int:
    min_area = m * n
    min_x = float('inf')
    min_y = float('inf')

    for o in ops:
        x, y = o
        area = x * y

        if x < min_x:
            min_x = x

        if y < min_y:
            min_y = y

    return min(min_area, min_x * min_y)


print(maxCount(m=3, n=3, ops=[[2, 2], [3, 3]]))
