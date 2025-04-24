"""
https://leetcode.com/problems/path-sum/description/

112. Path Sum
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that
adding up all the values along the path equals targetSum.
A leaf is a node with no children.

Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.

Example 2:
Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There are two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.

Example 3:
Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.

Constraints:
The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
"""
from binary_tree import TreeNode, createFromList


class Solution:
    def has_path_sum(self, root: TreeNode, targetSum: int) -> bool:
        """
        Since we've already completed path sum II, we could certainly accomplish the same thing with the same algo.
        Could we potentially make this algorithm a little smoother though?

        Maybe we could make this function be the dfs algo without a need to define a nested dfs algo.
        We could add and subtract from targetSum instead of appending and popping from a list.
        If we ever reached a child node where targetSum was 0, we would know that we could return True up the stack.
        At each TreeNode, we could just return dfs(left or dfs(right).

        Our base case is a leaf node. If targetSum equals 0 while we are at a leaf node, return True, otherwise False.
        """
        if not root: return False

        targetSum -= root.val

        if root.left == None and root.right == None:
            if targetSum == 0:
                return True
            return False

        left = self.has_path_sum(root.left, targetSum) if root.left else False
        right = self.has_path_sum(root.right, targetSum) if root.right else False

        return left or right


solution = Solution()

test_cases = [
    {
        "root": createFromList([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]),
        "targetSum": 22,
        "expected": True,
        "description": "Basic test with a valid path"
    },
    {
        "root": createFromList([1, 2, 3]),
        "targetSum": 5,
        "expected": False,
        "description": "No valid path"
    },
    {
        "root": createFromList([]),
        "targetSum": 0,
        "expected": False,
        "description": "Empty tree"
    },
    {
        "root": createFromList([5]),
        "targetSum": 5,
        "expected": True,
        "description": "Single node matching targetSum"
    },
    {
        "root": createFromList([5]),
        "targetSum": 10,
        "expected": False,
        "description": "Single node not matching targetSum"
    },
    {
        "root": createFromList([1, 2, 3, None, 5, None, 4]),
        "targetSum": 8,
        "expected": True,
        "description": "Multiple paths with the same targetSum"
    },
    {
        "root": createFromList([1, 2, 3, None, 5, None, 4]),
        "targetSum": 10,
        "expected": False,
        "description": "No path matches targetSum"
    }
]

for i, test in enumerate(test_cases, 1):
    result = solution.has_path_sum(test["root"], test["targetSum"])
    assert result == test["expected"], (
        f"Test {i} ({test['description']}) failed."
        f"Expected {test['expected']}, but got {result}"
    )

print("All tests passed!")
