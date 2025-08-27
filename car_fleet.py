def car_fleet(target, position, speed):
    pairs = [(p, s) for p, s in zip(position, speed)]
    pairs.sort(reverse=True)
    stack = []

    for p, s in pairs:
        time = (target - p) / s
        stack.append(time)

        # If the appended time is smaller than the previous
        # it means that the cars collide and become a fleet
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()

    return len(stack)


print(car_fleet(10, [1, 4], [3, 2]))
