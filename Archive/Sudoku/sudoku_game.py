from sudoku_graph import SudokuGraph


def testSudokuBoardGeneration(sudoku: SudokuGraph):    
    for i in range(100):
        sudoku.generateNewBoard()

sudoku = SudokuGraph()
# testSudokuBoardGeneration(sudoku)        


print(sudoku)

