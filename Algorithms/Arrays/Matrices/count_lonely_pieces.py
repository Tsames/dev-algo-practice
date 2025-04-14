"""
Formation Prompt:

In a game played on a 2d grid, there are blue pieces and red pieces for the two players. In this game a piece is
considered "lonely" if it is the only piece of that color in its row, and it's column. For example, in the following
board, the right-most R and B pieces that appear in a column are both lonely.

B R . . .
B . B R .
. R R B .

A a board represented with a two-dimensional array and a color, count the number of lonely pieces of that color on
the board. The colors will be represented by a single upper case character as in this example board and empty places
will be represented by a single period character.

Example(s)
b1 = [
  ['B', 'R', '.', '.', '.'],
  ['B', '.', 'B', 'R', '.'],
  ['.', 'R', 'R', 'B', '.'],
]

countLonelyPieces(b1, "R") -> 1
countLonelyPieces(b1, "B") -> 1

Signature/Prototype
function countLonelyPieces(board, color)
def count_lonely_pieces(board, color):
"""

class Solution:
    def count_lonely_pieces(self, board: list[list[str]], color: str) -> int:


solution = Solution()
# Test cases
tests = [
    {
        "board": [
            ['B', 'R', '.', '.', '.'],
            ['B', '.', 'B', 'R', '.'],
            ['.', 'R', 'R', 'B', '.']
        ],
        "color": "R",
        "expected": 1,
        "description": "Given example case for Red pieces"
    },
    {
        "board": [
            ['B', 'R', '.', '.', '.'],
            ['B', '.', 'B', 'R', '.'],
            ['.', 'R', 'R', 'B', '.']
        ],
        "color": "B",
        "expected": 1,
        "description": "Given example case for Blue pieces"
    },
    {
        "board": [
            ['B', '.', '.'],
            ['.', '.', '.'],
            ['.', '.', '.']
        ],
        "color": "B",
        "expected": 1,
        "description": "Single piece on board"
    },
    {
        "board": [
            ['B', 'B', 'B'],
            ['B', 'R', 'B'],
            ['B', 'B', 'B']
        ],
        "color": "R",
        "expected": 1,
        "description": "Surrounded piece"
    },
    {
        "board": [
            ['.', '.', '.'],
            ['.', '.', '.'],
            ['.', '.', '.']
        ],
        "color": "B",
        "expected": 0,
        "description": "Empty board"
    }
]

# Run tests
for i, test in enumerate(tests, 1):
    result = solution.count_lonely_pieces(test["board"], test["color"])
    assert result == test["expected"], (
        f"Test {i} ({test['description']}) failed. "
        f"Expected {test['expected']}, but got {result}"
    )

print("All tests passed!")