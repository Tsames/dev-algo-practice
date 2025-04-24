"""
https://leetcode.com/problems/path-sum-iii/description/

437. Path Sum III
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.
The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

Example 1:
Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.

Example 2:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3

Constraints:
The number of nodes in the tree is in the range [0, 1000].
-109 <= Node.val <= 109
-1000 <= targetSum <= 1000
"""
from binary_tree import TreeNode, createFromList

class Solution:
    def path_sum(self, root: TreeNode, targetSum: int) -> int:
        #Todo
        return 0

solution = Solution()

test_cases = [
    {
        "root": createFromList([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]),
        "targetSum": 8,
        "expected": 3,
        "description": "Basic test with multiple valid paths"
    },
    {
        "root": createFromList([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]),
        "targetSum": 22,
        "expected": 3,
        "description": "Multiple paths with the same targetSum"
    },
    {
        "root": createFromList([1, 2, 3]),
        "targetSum": 5,
        "expected": 0,
        "description": "No valid path"
    },
    {
        "root": createFromList([]),
        "targetSum": 0,
        "expected": 0,
        "description": "Empty tree"
    },
    {
        "root": createFromList([5]),
        "targetSum": 5,
        "expected": 1,
        "description": "Single node matching targetSum"
    },
    {
        "root": createFromList([5]),
        "targetSum": 10,
        "expected": 0,
        "description": "Single node not matching targetSum"
    },
    {
        "root": createFromList([1, -2, -3, 1, 3, -2, None, -1]),
        "targetSum": -1,
        "expected": 4,
        "description": "Negative values with multiple valid paths"
    }
]

for i, test in enumerate(test_cases, 1):
    result = solution.path_sum(test["root"], test["targetSum"])
    assert result == test["expected"], (
        f"Test {i} ({test['description']}) failed. "
        f"Expected {test['expected']}, but got {result}"
    )

print("All tests passed!")