from typing import List


def calPoints(operations: List[str]) -> int:
    records = []

    for o in operations:
        if o in "+DC":
            if o == "C":
                records.pop()
            elif o == "D":
                records.append(records[-1] * 2)
            else:
                records.append(records[-1] + records[-2])
        else:
            records.append(int(o))

    return sum(records)


print(calPoints(["5", "2", "C", "D", "+"]))
print(calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]))
