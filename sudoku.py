# Will solve any solvable sudoku problem
# Enter the puzzle in the sudoku_board variable and enter -1 for the unknown values

# Function to find the next empty (-1) slot
def find_next_empty(puzzle):
    for r in range(9):
        for c in range(9):
            # If empty slot is found, its location is returned. Else None is returned and the puzzle is solved
            if puzzle[r][c] == -1:
                return r, c
    return None, None


# Function to check if the guess made is valid
def is_valid(puzzle, guess, row, col):
    row_values = puzzle[row]
    # If the number guessed is already in the row/column/mini square then False is returned and another guess is made
    # If false is returned than the value is valid
    if guess in row_values:
        return False
    col_values = [puzzle[i][col] for i in range(9)]
    if guess in col_values:
        return False
    # Finding the 3x3 mini square location
    row_start = (row // 3)*3
    col_start = (col // 3)*3
    for r in range(row_start, row_start+3):
        for c in range(col_start, col_start+3):
            if puzzle[r][c] == guess:
                return False
    return True


# Function to generate the guesses
def solve_sudoku(puzzle):
    # Finding next empty slot - If None puzzle solved
    row, col = find_next_empty(puzzle)
    if row is None:
        return True

    # Recursion of the solve_sudoku function until the solution is found
    for guess in range(1, 10):
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            if solve_sudoku(puzzle):
                return True
        puzzle[row][col] = -1
    return False


if __name__ == '__main__':
    # Sudoku problem
    # -1 are the unknown numbers
    example_board = [
        [6, -1, -1, -1, -1, 5, -1, -1, -1],
        [-1, -1, -1, 3, -1, 9, -1, 5, -1],
        [-1, -1, -1, -1, 4, -1, -1, 6, -1],

        [4, -1, 3, -1, -1, -1, -1, -1, -1],
        [-1, 8, -1, 7, -1, -1, 2, -1, -1],
        [-1, -1, -1, -1, -1, 1, 7, -1, -1],

        [-1, -1, -1, -1, 9, -1, -1, -1, 6],
        [-1, -1, 5, -1, 2, -1, 8, 4, 9],
        [-1, 4, -1, -1, -1, 3, -1, -1, -1]
    ]
    for r in range(0, 9):
        for c in range(0, 9):
            if c == 3 or c == 6 or c == 9:
                print("|", end=" ")
            if example_board[r][c] == -1:
                print("0", end=" ")
            else:
                print(example_board[r][c], end=" ")
        print()
        if r == 2 or r == 5 or r == 8:
            print("_____________________")

    print(solve_sudoku(example_board))

    for r in range(0, 9):
        for c in range(0, 9):
            if c == 3 or c == 6 or c == 9:
                print("|", end=" ")
            if example_board[r][c] == -1:
                print("0", end=" ")
            else:
                print(example_board[r][c], end=" ")
        print()
        if r == 2 or r == 5 or r == 8:
            print("_____________________")
