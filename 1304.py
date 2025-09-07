from typing import List


def sumZero(n: int) -> List[int]:
    res = []

    for i in range(1, n // 2):
        res.append(i)
        res.append(-i)

    if n % 2 == 1:
        res.append(0)

    return res
