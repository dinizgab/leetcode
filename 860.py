from typing import List
from collections import defaultdict


def lemonadeChange(bills: List[int]) -> bool:
    cashier = defaultdict(int)

    for b in bills:
        cashier[b] += 1

        if b == 10:
            cashier[5] -= 1

            if cashier[5] < 0:
                return False
        elif b == 20:
            curr = 10 if cashier[10] > 0 else 5
            change = 15

            while change > 0:
                change -= curr
                cashier[curr] -= 1

                if cashier[curr] < 0:
                    return False

                if curr > change:
                    curr = 5

    return True


print(lemonadeChange([5, 5, 5, 10, 20]))
print(lemonadeChange([5, 5, 10, 10, 20]))
print(lemonadeChange([5, 5, 10, 20, 5, 5, 5, 5,
      5, 5, 5, 5, 5, 10, 5, 5, 20, 5, 20, 5]))
