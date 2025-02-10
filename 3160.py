def queryResults(limit, queries):
    # Map to keep track of the colors of each ball
    ball_colors = {}

    # Map to count how many of that label are there
    color_count = {}
    unique_colors = 0
    res = []

    for b, lab in queries:
        if b in ball_colors:
            prev = ball_colors[b]
            color_count[prev] -= 1

            if color_count[prev] == 0:
                unique_colors -= 1

        ball_colors[b] = lab
        if lab in color_count:
            color_count[lab] += 1
        else:
            color_count[lab] = 1

        if color_count[lab] == 1:
            unique_colors += 1

        res.append(unique_colors)

    return res


# This code works, but is not the most optimized one,
# because of the remove operation which is O(n)
# and the set() which is also O(n), making this solution
# O(n2), exceeding time limit
def queryResultON2(limit, queries):
    ball_colors = {}
    labels = []
    res = []

    for q in queries:
        b = q[0]
        lab = q[1]

        if b in ball_colors:
            labels.remove(ball_colors[b])  # O(n)

        ball_colors[b] = lab
        labels.append(lab)
        res.append(len(set(labels)))  # O(n)

    return res


print(queryResults(4, [[1, 4], [2, 5], [1, 3], [3, 4]]))
print(queryResults(4, [[0, 1], [1, 2], [2, 2], [3, 4], [4, 5]]))
print(queryResults(4, [[0, 1], [1, 4], [1, 1], [1, 4], [1, 1]]))
