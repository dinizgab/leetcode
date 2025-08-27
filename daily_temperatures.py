def daily_temperatures(temperatures):
    stack = []  # pair = (index, temperature)
    res = [0] * len(temperatures)

    for i in range(len(temperatures)):
        curr = temperatures[i]

        if not stack:
            stack.append((i, curr))
        else:
            # While our current is bigger than the temp at the top
            # of the stack, we pop and calculate the value at that index
            while stack and curr > stack[-1][1]:
                res[stack[-1][0]] = i - stack[-1][0]
                stack.pop()

            stack.append((i, curr))

    return res


print(daily_temperatures([30, 38, 30, 36, 35, 40, 28]))
