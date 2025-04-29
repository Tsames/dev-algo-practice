"""
https://leetcode.com/problems/jump-game/description/

55. Jump Game
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.

Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

Constraints:
1 <= nums.length <= 104
0 <= nums[i] <= 105
"""

class Solution:
    def can_jump(self, nums: list[int]) -> bool:
        #Todo
        return True

solution = Solution()

test_cases = [
    {
        "nums": [2, 3, 1, 1, 4],
        "expected": True,
        "description": "Basic test where the last index is reachable"
    },
    {
        "nums": [3, 2, 1, 0, 4],
        "expected": False,
        "description": "Test where the last index is not reachable"
    },
    {
        "nums": [0],
        "expected": True,
        "description": "Single element array, already at the last index"
    },
    {
        "nums": [2, 0, 0],
        "expected": True,
        "description": "Test where jumps exactly reach the last index"
    },
    {
        "nums": [1, 1, 0, 1],
        "expected": False,
        "description": "Test where a zero blocks progress to the last index"
    },
    {
        "nums": [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
        "expected": True,
        "description": "Large jump at the start allows reaching the last index"
    }
]

for i, test in enumerate(test_cases, 1):
    result = solution.can_jump(test["nums"])
    assert result == test["expected"], (
        f"Test {i} ({test['description']}) failed. "
        f"Expected {test['expected']}, but got {result}"
    )

print("All tests passed!")