"""
Formation Prompt:

In this task, we're going to apply basic 2-dimensional matrix traversals to solve some simple problems. While working
on these, look out for other patterns you may have seen previously. Each of these takes the row- and column-major
traversals and composites them with simpler ideas you have almost certainly encountered in one-dimensional array
problems.
This task is two similar problems in one:
First, write a function that returns the average of the smallest values in each column.
Write a new version of this function that returns the average of the smallest value in each row.

For example, if the for the matrix:
[[1, 5, 3]
 [4, 2, 6]]

The smallest values in each column are 1, 2, and 3. The average of these is 2.
Remember that since we represent a matrix as nested arrays (an array of arrays), many problems on a matrix can be
broken down into two array patterns. This makes them easier to reason about and code.

Example(s)
matrix = [
  [32, 23, 3],
  [23,  7, 5]
]

averageColumnMinimum(matrix) == 11 (because average(23, 7, 3) = 11)
averageRowMinimum(matrix) == 4 (because average(5, 3) = 4)

Signature/Prototype
function averageColumnMinimum(matrix) {
function averageRowMinimum(matrix) {

def averageColumnMinimum(matrix: list[list[int]]) -> float:
def averageRowMinimum(matrix: list[list[int]]) -> float:
"""


class Solution:
    def average_column_minimum(self, matrix: list[list[int]]) -> float:
        if not matrix:
            return 0.0

        min_total = 0

        for c in range(len(matrix[0])):
            col_min = float("inf")
            for r in range(len(matrix)):
                col_min = min(col_min, matrix[r][c])
            min_total += col_min

        return float(min_total / len(matrix[0]))

    def average_row_minimum(self, matrix: list[list[int]]) -> float:
        if not matrix:
            return 0.0

        min_total = 0

        for r in range(len(matrix)):
            row_min = float("inf")
            for c in range(len(matrix[0])):
                row_min = min(row_min, matrix[r][c])
            min_total += row_min

        return float(min_total / len(matrix))


solution = Solution()

test_cases = [
    {
        "matrix": [
            [1, 5, 3],
            [4, 2, 6]
        ],
        "col_min_expected": 2.0,  # min cols: (1,2,3) -> avg = 2.0
        "row_min_expected": 1.5,  # min rows: (1,2) -> avg = 1.5
        "description": "Basic 2x3 matrix"
    },
    {
        "matrix": [
            [32, 23, 3],
            [23, 7, 5]
        ],
        "col_min_expected": 11.0,  # min cols: (23,7,3) -> avg = 11.0
        "row_min_expected": 4.0,  # min rows: (3,5) -> avg = 4.0
        "description": "Example from prompt"
    },
    {
        "matrix": [[1]],
        "col_min_expected": 1.0,
        "row_min_expected": 1.0,
        "description": "Single element matrix"
    },
    {
        "matrix": [
            [10, 20],
            [30, 40],
            [50, 60]
        ],
        "col_min_expected": 15.0,  # min cols: (10,20) -> avg = 15.0
        "row_min_expected": 30.0,  # min rows: (10,30,50) -> avg = 30.0
        "description": "3x2 matrix"
    },
    {
        "matrix": [],
        "col_min_expected": 0.0,
        "row_min_expected": 0.0,
        "description": "Empty matrix"
    }
]

for i, test in enumerate(test_cases, 1):
    # Test column minimum average
    col_result = solution.average_column_minimum(test["matrix"])
    assert abs(col_result - test["col_min_expected"]) < 0.001, (
        f"Test {i} ({test['description']}) failed for column minimum average. "
        f"Expected {test['col_min_expected']}, but got {col_result}"
    )

    # Test row minimum average
    row_result = solution.average_row_minimum(test["matrix"])
    assert abs(row_result - test["row_min_expected"]) < 0.001, (
        f"Test {i} ({test['description']}) failed for row minimum average. "
        f"Expected {test['row_min_expected']}, but got {row_result}"
    )

print("All tests passed!")
