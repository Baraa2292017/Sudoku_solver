class SudokuSolver:
    @staticmethod
    def check_status(board):
        for row in range(0, 9):
            for column in range(0, 9):
                if board[row][column] == 0:
                    return False
        return True

    @staticmethod
    def print_board(board):

        for i in range(len(board)):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - - - ")

            for j in range(len(board[0])):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")

                if j == 8:
                    print(board[i][j])
                else:
                    print(str(board[i][j]) + " ", end="")

    @staticmethod
    def find_available_numbers(board, row, column):
        available = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        # traverse the row
        for i in board[row]:
            available[i] = 0

        # traverse the column
        for i in range(0, 9):
            for j in range(0, 9):
                if j < column:
                    continue
                elif j == column:
                    available[board[i][j]] = 0
                else:
                    break

        # # traverse the square
        if row <= 2:
            if column <= 2:
                for i in range(0, 3):
                    for j in range(0, 3):
                        available[board[i][j]] = 0

            elif column <= 5:
                for i in range(0, 3):
                    for j in range(3, 6):
                        available[board[i][j]] = 0
            else:
                for i in range(0, 3):
                    for j in range(6, 9):
                        available[board[i][j]] = 0

        elif row <= 5:
            if column <= 2:
                for i in range(3, 6):
                    for j in range(0, 3):
                        available[board[i][j]] = 0

            elif column <= 5:
                for i in range(3, 6):
                    for j in range(3, 6):
                        available[board[i][j]] = 0
            else:
                for i in range(3, 6):
                    for j in range(6, 9):
                        available[board[i][j]] = 0

        else:
            if column <= 2:
                for i in range(6, 9):
                    for j in range(0, 3):
                        available[board[i][j]] = 0

            elif column <= 5:
                for i in range(6, 9):
                    for j in range(3, 6):
                        available[board[i][j]] = 0
            else:
                for i in range(6, 9):
                    for j in range(6, 9):
                        available[board[i][j]] = 0

        # pop the zeros
        element = 0
        while element < len(available):
            if available[element] == 0:
                available.pop(element)
                continue
            element += 1
        return available.copy()

    @staticmethod
    def solve(board):
        # check if its done
        if SudokuSolver.check_status(board):
            print('After solving:')
            SudokuSolver.print_board(board)
            return True

        for row in range(0, 9):
            for column in range(0, 9):
                # if this is an empty cell
                if board[row][column] == 0:
                    # find all available numbers
                    available_numbers = SudokuSolver.find_available_numbers(board, row, column)
                    # print(f"available numbers for [{row}][{column}] = {available_numbers}")

                    if len(available_numbers) == 0:
                        return False
                    while len(available_numbers) > 0:
                        board[row][column] = available_numbers.pop()
                        answer = SudokuSolver.solve(board)
                        if not answer:
                            board[row][column] = 0
                            continue
                        else:
                            return True

                    return False
