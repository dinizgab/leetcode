def largest_rectangle_histogram(heights):
    stack = []
    max_area = 0

    for i, h in enumerate(heights):
        start = i
        while stack and h < stack[-1][1]:
            prev_index, prev_height = stack.pop()
            max_area = max(max_area, (i - prev_index) * h)
            start = prev_index

        stack.append((start, h))

    for i, h in stack:
        max_area = max(max_area, h * (len(heights) - i))

    return max_area


print(largest_rectangle_histogram([2, 1, 5, 6, 2, 3]))
