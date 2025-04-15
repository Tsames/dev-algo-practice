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
        """
        The trick to this algorithm is that we don't want to end up doing repeated checks for each occurrence of 'B'
        or 'R' that we come across. That would be the brute force solution.

        So, how could we prevent ourselves from having to repeatedly iterate through the same row and column?
        What if we use an array of set to keep track of the pieces in each column?
        We'd have an array of length m where m is the length of board[0] with a set at each index.
        We'd have a similar set for each row.

        Then we would iterate through our board. Each time we find a non-empty tile, we add it to the two
        corresponding sets.
        The problem with where this solution is going comes with when you know to add to your lonely pieces count.
        We can't add to the count for the first piece we encounter because we don't yet know if its the last
        occurrence in that row/column.

        Instead of sets, we could use arrays of hashmaps.
        Our first iteration we would simply add to hashmaps.
        Our second iteration, we could check the hashmaps and add to our total if both corresponding hashmaps only
        contained a count of 1 for the number we were interested in.

        This would be O(n) time complexity, rather O(n * r * c) where n is the total elements in our matrix and r is
        the total element in a given row, and c is the total elements in a given col.
        """
        if not board:
            return 0

        rows = [{} for _ in board]
        cols = [{} for _ in board[0]]

        # Fill up the count for our hashmaps
        for r in range(len(board)):
            for c in range(len(board[0])):
                piece = board[r][c]
                if piece != ".":
                    rows[r][piece] = 1 + rows[r].get(piece, 0)
                    cols[c][piece] = 1 + cols[c].get(piece, 0)

        res = 0
        for r in range(len(board)):
            for c in range(len(board[0])):
                piece = board[r][c]
                if piece == color and rows[r].get(piece) == 1 and cols[c].get(piece) == 1:
                    res += 1

        return res

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