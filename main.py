def printGrid(arr):
    for i in range(9):
        for j in range(9):
            print(arr[i][j], end=" ")
        print()


def isSafe(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False
        if grid[x][col] == num:
            return False

    start_row = row - row % 3
    start_col = col - col % 3

    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] == num:
                return False
    return True


def f_free(grid):
    for i in range(0, 9, 1):
        for j in range(0, 9, 1):
            if grid[i][j] == 0:
                return [i, j]
    return [9, 9]


def solve_sudoku(sudoku):
    row = f_free(sudoku)[0]
    col = f_free(sudoku)[1]

    if col == 9:
        yield sudoku
    else:
        for num in range(1, 10, 1):
            if isSafe(sudoku, row, col, num):
                sudoku[row][col] = num
                yield from solve_sudoku(sudoku)
            sudoku[row][col] = 0

it = solve_sudoku([[0 for x in range(9)] for y in range(9)])

for x in range(4):
    printGrid(next(it))
    print()
