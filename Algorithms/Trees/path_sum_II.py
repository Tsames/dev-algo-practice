"""
https://leetcode.com/problems/path-sum-ii/description/

113. Path Sum II
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node
values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.
A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22

Example 2:
Input: root = [1,2,3], targetSum = 5
Output: []

Example 3:
Input: root = [1,2], targetSum = 0
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
"""
from binary_tree import TreeNode, createFromList


class Solution:
    def path_sum(self, root: TreeNode, targetSum: int) -> list[list[int]]:
        if not root: return []

        res = []
        path = []

        def dfs(root: TreeNode):
            path.append(root.val)
            if root.left == None and root.right == None:
                if sum(path) == targetSum:
                    res.append(path.copy())
                return

            if root.left != None:
                dfs(root.left)
                path.pop()

            if root.right != None:
                dfs(root.right)
                path.pop()

        dfs(root)
        return res

solution = Solution()

test_cases = [
    {
        "root": createFromList([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]),
        "targetSum": 22,
        "expected": [[5, 4, 11, 2], [5, 8, 4, 5]],
        "description": "Basic test with multiple valid paths"
    },
    {
        "root": createFromList([1, 2, 3]),
        "targetSum": 5,
        "expected": [],
        "description": "No valid path"
    },
    {
        "root": createFromList([1, 2]),
        "targetSum": 0,
        "expected": [],
        "description": "Empty result with no valid path"
    },
    {
        "root": None,
        "targetSum": 0,
        "expected": [],
        "description": "Empty tree"
    },
    {
        "root": createFromList([5]),
        "targetSum": 5,
        "expected": [[5]],
        "description": "Single node matching targetSum"
    },
    {
        "root": createFromList([5]),
        "targetSum": 10,
        "expected": [],
        "description": "Single node not matching targetSum"
    },
    {
        "root": createFromList([1, 2, 3, None, 5, None, 4]),
        "targetSum": 8,
        "expected": [[1, 2, 5], [1, 3, 4]],
        "description": "Multiple paths with the same targetSum"
    }
]

for i, test in enumerate(test_cases, 1):
    result = solution.path_sum(test["root"], test["targetSum"])
    assert result == test["expected"], (
        f"Test {i} ({test['description']}) failed. "
        f"Expected {test['expected']}, but got {result}"
    )

print("All tests passed!")
