"""
https://neetcode.io/problems/search-2d-matrix

Search 2D Matrix

You are given an m x n 2-D integer array matrix and an integer target.
Each row in matrix is sorted in non-decreasing order.
The first integer of every row is greater than the last integer of the previous row.
Return true if target exists within matrix or false otherwise.

Can you write a solution that runs in O(log(m * n)) time?

Example 1:
Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10
Output: true

Example 2:
Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15
Output: false

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-10000 <= matrix[i][j], target <= 10000
"""

from math import floor


class Solution:
    """
    First we can conduct binary search on the rows themselves.
    Since we know that the first element of each row within our matrix contains an element that
    is larger than the last element of the row before it,
    we can safely compare our target to the first element of that row.
    """

    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # Use Binary Search to find the row that our target is in,
        top, bottom = 0, len(matrix) - 1

        while top <= bottom:
            row = (top + bottom) // 2

            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break

        # return False if the row doesn't exist
        if not (top <= bottom):
            return False


        # Use Binary Search to find the target within the row,
        left, right = 0, len(matrix[0]) - 1
        row = (top + bottom) // 2
        
        while left <= right:
            mid = (left + right) // 2

            if target == matrix[row][mid]:
                return True
            elif target < matrix[row][mid]:
                right = mid - 1
            else:
                left = mid + 1

        #Exhausted the targeted row without finding our target, so return False
        return False


solution = Solution()
print(
    solution.searchMatrix(
        [
            [1, 2, 4, 8],
            [10, 11, 12, 13],
            [14, 20, 30, 40],
            [50, 60, 70, 80, 90, 100, 101, 102],
            [105, 106, 201, 202, 203, 204, 301],
        ],
        303,
    )
)

print(
    solution.searchMatrix(
        [
            [1, 2, 4, 8],
            [10, 11, 12, 13],
            [14, 20, 30, 40],
            [50, 60, 70, 80, 90, 100, 101, 102],
            [105, 106, 201, 202, 203, 204, 301],
        ],
        50,
    )
)
