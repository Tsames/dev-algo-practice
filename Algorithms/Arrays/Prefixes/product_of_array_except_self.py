"""
https://leetcode.com/problems/product-of-array-except-self/description/

238. Product of Array Except Self
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:
2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""

class Solution():
    def product_except_self(self, nums: list[int]) -> list[int]:
        # Todo

# Tests for product_of_array_except_self.py
solution = Solution()

test_cases = [
    {"nums": [1, 2, 3, 4], "expected": [24, 12, 8, 6], "description": "Example from problem statement"},
    {"nums": [-1, 1, 0, -3, 3], "expected": [0, 0, 9, 0, 0], "description": "Array with zero"},
    {"nums": [1, 1], "expected": [1, 1], "description": "Minimum length array"},
    {"nums": [2, 3, 4, 5], "expected": [60, 40, 30, 24], "description": "All positive integers"},
    {"nums": [-2, -3, -4], "expected": [-12, -8, -6], "description": "All negative integers"},
    {"nums": [-1, 1, -1, 1], "expected": [-1, -1, -1, -1], "description": "Alternating signs"},
    {"nums": [0, 0, 0, 0], "expected": [0, 0, 0, 0], "description": "All zeros"},
    {"nums": [10, 3, 5, 6, 2], "expected": [180, 600, 360, 300, 900], "description": "Larger numbers"},
    {"nums": [0, 1, 2, 0], "expected": [0, 0, 0, 0], "description": "Multiple zeros"}
]

for i, test in enumerate(test_cases, 1):
    nums = test["nums"]
    expected = test["expected"]
    actual = solution.product_except_self(nums)
    assert actual == expected, f"Test {i} ({test['description']}) failed. Expected: {expected}, but got: {actual}"

print("All tests passed!")