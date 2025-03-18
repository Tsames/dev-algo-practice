'''
https://neetcode.io/problems/balanced-binary-tree

Balanced Binary Tree
Given a binary tree, return true if it is height-balanced and false otherwise.
A height-balanced binary tree is defined as a binary tree in which the left and right
subtrees of every node differ in height by no more than 1.

Example 1:
Input: root = [1,2,3,null,null,4]
Output: true

Example 2:
Input: root = [1,2,3,null,null,4,null,5]
Output: false

Example 3:
Input: root = []
Output: true

Constraints:
The number of nodes in the tree is in the range [0, 1000].
-1000 <= Node.val <= 1000
'''

from typing import Optional
from binary_tree import TreeNode, createFromList

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root) -> list[int, bool]:
            if not root:
               return 0

            left = dfs(root.left)
            right = dfs(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1

            return max(left, right) + 1

        return dfs(root) != -1

solution = Solution()

# Test case 1: Example from problem statement
expected = True
tree = createFromList([1, 2, 3, None, None, 4])
actual = solution.isBalanced(tree)
assert actual == expected, f"Test one failed. Expected: {expected}, but got: {actual}"

# Test case 2: Example from problem statement - unbalanced tree
expected = False
tree = createFromList([1, 2, 3, None, None, 4, None, 5])
actual = solution.isBalanced(tree)
assert actual == expected, f"Test two failed. Expected: {expected}, but got: {actual}"

# Test case 3: Empty tree
expected = True
tree = createFromList([])
actual = solution.isBalanced(tree)
assert actual == expected, f"Test three failed. Expected: {expected}, but got: {actual}"

# Test case 4: Perfect balanced tree
expected = True
tree = createFromList([1, 2, 3, 4, 5, 6, 7])
actual = solution.isBalanced(tree)
assert actual == expected, f"Test four failed. Expected: {expected}, but got: {actual}"

# Test case 5: Single node tree
expected = True
tree = createFromList([1])
actual = solution.isBalanced(tree)
assert actual == expected, f"Test five failed. Expected: {expected}, but got: {actual}"

# Test case 6: Left-heavy unbalanced tree
expected = False
tree = createFromList([1,2,2,3,None,None,3,4,None,None,4])
actual = solution.isBalanced(tree)
assert actual == expected, f"Test six failed. Expected: {expected}, but got: {actual}"

print("All tests passed!")