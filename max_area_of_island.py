def max_area_of_island(grid):
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    ROWS, COLS = len(grid), len(grid[0])
    max_island = 0

    def dfs(i, j, curr_size):
        nonlocal max_island

        if i >= ROWS or j >= COLS or grid[i][j] == 0 or i < 0 or j < 0:
            max_island = max(max_island, curr_size)
            return

        grid[i][j] = 0
        for di, dj in directions:
            dfs(i + di, j + dj, curr_size + 1)

    for i in range(ROWS):
        for j in range(COLS):
            if grid[i][j] == 1:
                dfs(i, j, 1)

    return max_island


grid = [
    [0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [0, 1, 1, 0, 1],
    [0, 1, 0, 0, 1]
]

print(max_area_of_island(grid))
