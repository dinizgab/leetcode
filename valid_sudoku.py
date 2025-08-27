def valid_sudoku(board):
    n = len(board)
    # Check rows
    for i in range(n):
        row = [n for n in board[i] if n != "."]

        if len(set(row)) < len(row):
            return False

    # Check columns
    for i in range(n):
        seen = set()
        for j in range(n):
            if board[j][i] == ".":
                continue

            if board[j][i] in seen:
                return False

            seen.add(board[j][i])

    # for each row of the board
    # it is based in the row that we will get the
    # corresponding square of the board
    for square in range(n):
        seen = set()

        # for each row of the square
        for i in range(3):
            # for each col of the square
            for j in range(3):
                row = (square // 3) * 3 + i
                col = (square % 3) * 3 + j
                if board[row][col] == ".":
                    continue

                if board[row][col] in seen:
                    return False

                seen.add(board[row][col])

    return True


valid_board = board = [["1", "2", ".", ".", "3", ".", ".", ".", "."],
                       ["4", ".", ".", "5", ".", ".", ".", ".", "."],
                       [".", "9", "8", ".", ".", ".", ".", ".", "3"],
                       ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
                       [".", ".", ".", "8", ".", "3", ".", ".", "5"],
                       ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                       [".", ".", ".", ".", ".", ".", "2", ".", "."],
                       [".", ".", ".", "4", "1", "9", ".", ".", "8"],
                       [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

invalid_board = [["1", "2", ".", ".", "3", ".", ".", ".", "."],
                 ["4", ".", ".", "5", ".", ".", ".", ".", "."],
                 [".", "9", "1", ".", ".", ".", ".", ".", "3"],
                 ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
                 [".", ".", ".", "8", ".", "3", ".", ".", "5"],
                 ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                 [".", ".", ".", ".", ".", ".", "2", ".", "."],
                 [".", ".", ".", "4", "1", "9", ".", ".", "8"],
                 [".", ".", ".", ".", "8", ".", ".", "7", "9"]]


print(valid_sudoku(valid_board))
print(valid_sudoku(invalid_board))
