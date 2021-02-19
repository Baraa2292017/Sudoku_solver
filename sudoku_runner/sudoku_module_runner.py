from sudoku_module.sudoku_solver import SudokuSolver


class SudokuModuleRunner:
    @staticmethod
    def start(board):
        print('before solving:')
        SudokuSolver.print_board(board)
        print()
        SudokuSolver.solve(board)
