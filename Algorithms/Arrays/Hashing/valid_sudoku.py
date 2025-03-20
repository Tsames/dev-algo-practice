"""
https://leetcode.com/problems/valid-sudoku/description/
https://neetcode.io/problems/valid-sudoku

Valid Sudoku
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated
according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without
repetition.

Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Example 1:
Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified
to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

Constraints:
board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
"""

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        """
        Since Sudoku requires that no numbers repeat, and we are only checking the
        exisiting cells, we could make sets for each row, column, and square that we
        need to check (by square I mean a 3x3 subgrid).

        While iterating over those indecies, we would just add to and check our sets.
        If we ever found an element that already exists in our sets, we could break and
        return false.
        Otherwise, we return true if we get through all the iterations.

        The only tricky part with this solution is how do we know what square we are
        iterating inside?
        So how could we calculate this?
        The column index // 3 would give us 0, 1, or 2
        The row index // 3 would also give us 0, 1, or 2
        We can't just add the row and column indexes after the floor division to get
        the square index.
        We have to find another way.
        We would want to start with the row index after floor division times three to
        get the starting square in the row's index.
        Then we would add the column index after floor division to get the square's
        position.
        """

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                tile = board[row][col]
                if tile == ".":
                    continue

                square = 3 * (row // 3) + (col // 3)
                if tile in rows[row] or tile in cols[col] or tile in squares[square]:
                    return False

                rows[row].add(tile)
                cols[col].add(tile)
                squares[square].add(tile)

        return True

solution = Solution()

# Test case 1: Example from problem statement (valid board)
board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
expected = True
actual = solution.isValidSudoku(board)
assert actual == expected, f"Test 1 failed. Expected: {expected}, but got: {actual}"

# Test case 2: Example from problem statement (invalid board due to duplicate in
# top-left 3x3 sub-box)
board = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
expected = False
actual = solution.isValidSudoku(board)
assert actual == expected, f"Test 2 failed. Expected: {expected}, but got: {actual}"

# Test case 3: Empty board (valid, since no duplicates)
board = [
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."]
]
expected = True
actual = solution.isValidSudoku(board)
assert actual == expected, f"Test 3 failed. Expected: {expected}, but got: {actual}"

# Test case 4: Valid board with a specific pattern (all rows, columns, and sub-boxes
# are valid)
board = [
    ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
    ["4", "5", "6", "7", "8", "9", "1", "2", "3"],
    ["7", "8", "9", "1", "2", "3", "4", "5", "6"],
    ["2", "3", "4", "5", "6", "7", "8", "9", "1"],
    ["5", "6", "7", "8", "9", "1", "2", "3", "4"],
    ["8", "9", "1", "2", "3", "4", "5", "6", "7"],
    ["3", "4", "5", "6", "7", "8", "9", "1", "2"],
    ["6", "7", "8", "9", "1", "2", "3", "4", "5"],
    ["9", "1", "2", "3", "4", "5", "6", "7", "8"]
]
expected = True
actual = solution.isValidSudoku(board)
assert actual == expected, f"Test 4 failed. Expected: {expected}, but got: {actual}"

# Test case 5: Invalid board due to duplicate in a row
board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "7"]  # Duplicate '7' in the last row
]
expected = False
actual = solution.isValidSudoku(board)
assert actual == expected, f"Test 5 failed. Expected: {expected}, but got: {actual}"

# Test case 6: Invalid board due to duplicate in a column
board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "6"]  # Duplicate '6' in the last column
]
expected = False
actual = solution.isValidSudoku(board)
assert actual == expected, f"Test 6 failed. Expected: {expected}, but got: {actual}"

print("All tests passed!")
