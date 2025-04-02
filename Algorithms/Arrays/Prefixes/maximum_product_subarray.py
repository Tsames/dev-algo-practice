"""
https://leetcode.com/problems/maximum-product-subarray/description/

Maximum Product Subarray
Given an integer array nums, find a subarray that has the largest product, and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer.

Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

Constraints:
1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any subarray of nums is guaranteed to fit in a 32-bit integer.
"""
class Solution:
    def max_product(self, nums: list[int]) -> int:

solution = Solution()

test_cases = [
    {"nums": [2, 3, -2, 4], "expected": 6, "description": "Example from problem statement"},
    {"nums": [-2, 0, -1], "expected": 0, "description": "Example from problem statement"},
    {"nums": [0, 2], "expected": 2, "description": "Single positive number with zero"},
    {"nums": [-2, -3, 7], "expected": 42, "description": "Two negative numbers with a positive number"},
    {"nums": [-2, -3, 0, 7], "expected": 7, "description": "Two negative numbers with zero and a positive number"},
    {"nums": [2, 3, -2, 4, -1], "expected": 48, "description": "Mix of positive and negative numbers"},
    {"nums": [-1, -3, -10, 0, 60], "expected": 60, "description": "Negative numbers with zero and a large positive number"},
    {"nums": [-2, -3, 0, -2, -40], "expected": 80, "description": "Negative numbers with zero and a large negative number (2)"},
    {"nums": [1, 2, 3, 4], "expected": 24, "description": "All positive numbers"},
    {"nums": [-1, -2, -3, -4], "expected": 24, "description": "All negative numbers"}
]

for i, test in enumerate(test_cases, 1):
    nums = test["nums"]
    expected = test["expected"]
    actual = solution.max_product(nums)
    assert actual == expected, f"Test {i} ({test['description']}) failed. Expected: {expected}, but got: {actual}"

print("All tests passed!")