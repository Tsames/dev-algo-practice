"""
https://leetcode.com/problems/range-sum-query-2d-immutable/description/

Range Sum Query 2D - Immutable
Given a 2D matrix, handle multiple queries of the following type:

Calculate the sum of the elements of matrix inside the rectangle defined by its upper
left corner (row1, col1) and lower right corner (row2, col2).
Implement the NumMatrix class:

NumMatrix(int[][] matrix) Initializes the object with the integer matrix.
int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements
of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower
right corner (row2, col2).
You must design an algorithm where sumRegion works on O(1) time complexity.

Example 1:
Input
["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
[[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0,
5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
Output
[null, 8, 11, 12]

Explanation
NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5],
[4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle)
numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangle)

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
-104 <= matrix[i][j] <= 104
0 <= row1 <= row2 < m
0 <= col1 <= col2 < n
At most 104 calls will be made to sumRegion.
"""

class NumMatrix(object):
    def __init__(self, matrix):
        row, col = len(matrix), len(matrix[0])
        """
        The prefix matrix that we generate has one additional row and col filled 
        entirely with zeros so that when we try to calculate prefixes for the zeroth 
        index row or column on the original input matrix we don't get an out of bounds 
        error.
        """
        self.prefix_matrix = [[0] * (col + 1) for _ in range(row + 1)]
        """
        Now we fill our prefix matrix (except for the zeroth row and column which 
        remain all zeros) with the prefix as if that tile was the bottom right hand 
        corner and the top left hand corner was (1,1)
        """
        for r in range(row):
            prefix = 0
            for c in range(col):
                prefix += matrix[r][c]
                above = self.prefix_matrix[r][c + 1]
                self.prefix_matrix[r + 1][c + 1] = prefix + above

    def sumregion(self, row1, col1, row2, col2):
        # Translate our input indecies
        r1,c1,r2,c2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        """
        with our prefix matrix calculated in the init, we are now ready to repeatedly
        calculate the prefix sum of given upper lef hand and lower right hand
        coordinates in constant time.

        to do so we first take our the prefix of our lower right hand corner.
        then we subtract the box to the left of it.
        then we subtract the box above it.
        then we add the portion of those boxes that has been subtracted twice to cancel
        that operation out.
        """
        # the left box is the prefix in the same row as our lower right hand corner,
        # but one column over from our upper left hand corner.
        left_box = self.prefix_matrix[r2][c1 - 1]
        # the above box is the prefix in the same col as our lower right hand corner,
        # but one row above our upper left hand corner
        above_box = self.prefix_matrix[r1 - 1][c2]
        # the overlapping box is one row and col above our upper left hand corner
        overlapping_box = self.prefix_matrix[r1 - 1][c1 - 1]
        return self.prefix_matrix[r2][c2] - left_box - above_box + overlapping_box

matrix = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
]

solution = NumMatrix(matrix)

# Test 1: Original example from problem statement
assert solution.sumregion(2, 1, 4, 3) == 8, "Test 1 Failed: Example region 1"

# Test 2: Single element region
assert solution.sumregion(0, 0, 0, 0) == 3, "Test 2 Failed: Single element"

# Test 3: Entire matrix
assert solution.sumregion(0, 0, 4, 4) == 58, "Test 3 Failed: Entire matrix"

# Test 4: Single row
assert solution.sumregion(1, 0, 1, 4) == 17, "Test 4 Failed: Single row"

# Test 5: Single column
assert solution.sumregion(0, 2, 4, 2) == 7, "Test 5 Failed: Single column"

# Test 6: Top-left quadrant
assert solution.sumregion(0, 0, 1, 1) == 14, "Test 6 Failed: Top-left quadrant"

# Test 7: Top-right quadrant
assert solution.sumregion(0, 3, 1, 4) == 9, "Test 7 Failed: Top-right quadrant"

# Test 8: Bottom-left quadrant
assert solution.sumregion(3, 0, 4, 1) == 6, "Test 8 Failed: Bottom-left quadrant"

# Test 9: Bottom-right quadrant
assert solution.sumregion(3, 3, 4, 4) == 13, "Test 9 Failed: Bottom-right quadrant"

print("All tests passed!")