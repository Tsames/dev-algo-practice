"""
https://leetcode.com/problems/path-sum-iii/description/

437. Path Sum III
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values
along the path equals targetSum.
The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from
parent nodes to child nodes).

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
        """
        This problem is different from path sum two as it no longer requires that the path start from our root and
        end with a leaf node.

        We still have to return all the paths that satisfy our condition, but instead of the path represented as a
        list of the node values, we are simply recording the number of paths as an int return value.
        We are given the additional condition that a path cannot backtrack. All valid paths must always progress from
        parent to child. Which will drastically limit the number of possible paths that we have to consider. phew.

        This is tricky. For any given node that isn't our root we have to consider paths that both include all
        parents, some parents, and paths that start with the current node.

        We certainly still want to use dfs as our way to traverse our tree. The main question becomes 'how do we keep
        track of the path in such a way that it allows for us to consider so many options efficiently?'.

        In path sum two we used a list. This seems like it could still work, but might not be that efficient.
        If we look at the first given example, once we reach the node with value 3 on the third level we would have
        to iterate through our array to see if the entire sum equalled our target, then if just the parent and the
        current node equaled our target, and lastly if just the current node equalled our target.

        That's a lot of repeated calculation. Makes me think that maybe we could use a running total variable with a
        prefix list. Instead of the individual values, we construct our prefix list like this:

        [10,5,3] (old method - no prefixes)
        [0, 10, 15, 18] (prefix list) {add a zero to make calculations easier}

        Now we can start at the last index and subtract from it each of the previous indexes and compare that to the
        targetSum

        18 - 15 = 3 (current node's value)
        18 - 10 = 8 (parent and current node path's value)
        18 - 0 = 18 (root, direct parent, and current node's value)

        If we found a match, we could increment an outside variable.
        """
        if not root: return 0

        res = 0
        path = [0]

        def dfs(root: TreeNode):
            nonlocal res
            path.append(path[-1] + root.val)

            # Iterate through path (which is a prefix list) up until the second to last value
            for i in range(len(path) - 1):
                if path[-1] - path[i] == targetSum:
                    res += 1

            # Base Case - leaf node.
            # No return value because we don't care about the return value
            if not root.left and not root.right:
                return

            if root.left:
                dfs(root.left)
                path.pop()

            if root.right:
                dfs(root.right)
                path.pop()

        dfs(root)
        return res

    def path_sum_faster(self, root: TreeNode, targetSum: int) -> int:
        """
        Can we improve this algo by using a hashmap to hold our prefixes rather than a list?

        I think we could. The part of the previous algo attempt that slows it down is looping through our prefix array.
        What we really want to know at any given node is if there is a prefix that is equal to the difference between
        the current sum and targetSum.
        If we stored and removed our prefixes from a hashmap, we could improve our time complexity without
        sacrificing space complexity.
        """
        if not root: return 0

        res = 0
        # Initialize path with a count of 0 of 1. This makes the calculation in our dfs for the entirety of the path
        # possible without adjusting the logic.
        path = {0: 1}

        # Add a total variable to keep a running total
        def dfs(root: TreeNode, total):
            nonlocal res
            total = total + root.val

            path[total] = 1 + path.get(total, 0)

            # Check if there is a prefix in our current path that is equal to the difference between
            # total and targetSum, if there is, there is a path ending in the current node that satisfies our conditions
            if total - targetSum in path:
                res += 1

            if root.left: dfs(root.left, total)

            if root.right: dfs(root.right, total)

            path[total] -= 1

        dfs(root, 0)
        return res


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

for i, test in enumerate(test_cases, 1):
    result = solution.path_sum_faster(test["root"], test["targetSum"])
    assert result == test["expected"], (
        f"Test {i} ({test['description']}) failed. "
        f"Expected {test['expected']}, but got {result}"
    )

print("All tests passed!")
