from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals = sorted(intervals, key=lambda x: x[0])
    res = [intervals[0]]

    for start, end in intervals[1:]:
        last_end = intervals[-1][1]

        if start <= last_end:
            res[-1][1] = max(last_end, end)
        else:
            res.append([start, end])

    return res
