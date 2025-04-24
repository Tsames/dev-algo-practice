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
        '''
        Assumptions/Constraints/Edge Cases:
        - Can be given a root value that is null
        - Could also be given a binary tree that is just a single node
        - Not guaranteed that there is a single path that satisfies the sum condition (return empty list)

        - Need to return all root-to-leaf paths that sum to the targetSum
        - Cannot return a path that ends at a node that is not a leaf

        Thinking depth first search in general because we are loooking for paths to leaf nodes.
        If we used breadth first search, we wouldn't be traversing along paths like these. We would be traversing the
        tree level by level, which doesn't help us for this algo.

        Outline:

        If root is null, then return [] (edge case)

        We want an outter function that decalres a result list, this will hold all other paths that we find and be
        our return
        output

        We declare a list our dfs sub-algo will be using to determine if it satisfies the summing condition. (We'll
        append
        and pop to and from as we go through our dfs) path

        We want to define a dfs,
            I believe, append to path

            if we hit a leaf node, we want to do our calculation, and potentially append to res (copy of path)

            if the node we're visiting is null, then return

            if left child exist, call dfs on left
            pop the last element off of path

            if right child exists, call dfs on right
            pop the last element off of path

        dfs(root)
        return res
        '''
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
