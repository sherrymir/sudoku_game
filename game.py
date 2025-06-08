from board import print_sudoku, copy_and_add_number, create_empty_grid
from validator import sudoku_grid_correct

def play_sudoku():
    sudoku = create_empty_grid()

    while True:
        print_sudoku(sudoku)
        try:
            row = int(input("Enter row (0-8): "))
            col = int(input("Enter column (0-8): "))
            value = int(input("Enter value (1-9): "))

            if not (0 <= row <= 8 and 0 <= col <= 8 and 1 <= value <= 9):
                print("❌ Invalid input range. Try again.")
                continue

            if sudoku[row][col] != 0:
                print("❌ Cell already filled. Choose another.")
                continue

            trial = copy_and_add_number(sudoku, row, col, value)
            if sudoku_grid_correct(trial):
                sudoku = trial
            else:
                print("❌ That move breaks Sudoku rules!")

            if all(all(cell != 0 for cell in row) for row in sudoku) and sudoku_grid_correct(sudoku):
                print_sudoku(sudoku)
                print("🎉 You completed the Sudoku correctly!")
                break

        except ValueError:
            print("❌ Please enter valid numbers.")
