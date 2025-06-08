import copy

def print_sudoku(sudoku: list):
    for i, row in enumerate(sudoku):
        for j, col in enumerate(row):
            print("_" if col == 0 else col, end=" ")
            if (j + 1) % 3 == 0 and j < 8:
                print(" ", end="")
        print()
        if (i + 1) % 3 == 0 and i < 8:
            print()

def copy_and_add_number(sudo: list, row: int, col: int, value: int):
    sudoku = copy.deepcopy(sudo)
    sudoku[row][col] = value
    return sudoku

def create_empty_grid():
    return [[0 for _ in range(9)] for _ in range(9)]

