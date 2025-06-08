def sudoku_grid_correct(sudoku: list):

    def row_correct(sudoku: list, row_no: int):
        seen = set()
        for i in sudoku[row_no]:
            if i != 0:
                if i in seen:
                    return False
                seen.add(i)
        return True

    def col_correct(sudoku: list, col_no: int):
        seen = set()
        for row in sudoku:
            value = row[col_no]
            if value != 0:
                if value in seen:
                    return False
                seen.add(value)
        return True

    def block_correct(sudoku: list, row_no: int, col_no: int):
        seen = set()
        for row in range(row_no, row_no + 3):
            for col in range(col_no, col_no + 3):
                value = sudoku[row][col]
                if value != 0:
                    if value in seen:
                        return False
                    seen.add(value)
        return True

    for i in range(9):
        if not row_correct(sudoku, i) or not col_correct(sudoku, i):
            return False

    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            if not block_correct(sudoku, row, col):
                return False

    return True
