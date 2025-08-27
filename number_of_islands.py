def numbers_of_islands(grid):
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    ROWS, COLS = len(grid), len(grid[0])
    islands = 0

    def dfs(i, j):
        if i < 0 or i >= ROWS or j >= COLS or j < 0 or grid[i][j] == "0":
            return

        grid[i][j] = "0"
        for di, dj in directions:
            dfs(i + di, j + dj)

    for i in range(ROWS):
        for j in range(COLS):
            if grid[i][j] == "1":
                islands += 1
                dfs(i, j)

    return islands
