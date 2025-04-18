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
        """
        Notably we don't have to concern ourselves with the indices that make the subarray with the greatest product. We
        only have to find what that product is and return it.

        This is a bit similar to the max_subarray.py problem, but multiplication makes it a bit different since we can't
        just discard negative numbers and move on (multiples of 2 negative numbers give us a greater product).

        The contextual insights with multiplication is that once we encounter a 0 it essentially divides our array
        into two sub-arrays since including a 0 will make our product 0.

       The other key insight here is to keep track of the current max and min product as you move through the input
       array.
       This allows you to handle negative numbers very easily as they oscillate between a positive and negative product.

       The other thing to consider is that the number you encounter by itself may be the largest (this is the case if
       you run into a zero, or you start with a negative number - where both min and max are then negative).
        """
        res = float("-inf")
        cur_min, cur_max = 1, 1

        for n in nums:
            tmp = n * cur_max
            cur_max = max(tmp, n * cur_min, n)
            cur_min = min(tmp, n * cur_min, n)
            res = max(res, cur_max)

        return res


solution = Solution()

test_cases = [
    {"nums": [2, 3, -2, 4], "expected": 6, "description": "Example from problem statement"},
    {"nums": [-2, 0, -1], "expected": 0, "description": "Example from problem statement"},
    {"nums": [0, 2], "expected": 2, "description": "Single positive number with zero"},
    {"nums": [-2, -3, 7], "expected": 42, "description": "Two negative numbers with a positive number"},
    {"nums": [-2, -3, 0, 7], "expected": 7, "description": "Two negative numbers with zero and a positive number"},
    {"nums": [2, 3, -2, 4, -1], "expected": 48, "description": "Mix of positive and negative numbers"},
    {"nums": [-1, -3, -10, 0, 60], "expected": 60,
     "description": "Negative numbers with zero and a large positive number"},
    {"nums": [-2, -3, 0, -2, -40], "expected": 80,
     "description": "Negative numbers with zero and a large negative number (2)"},
    {"nums": [1, 2, 3, 4], "expected": 24, "description": "All positive numbers"},
    {"nums": [-1, -2, -3, -4], "expected": 24, "description": "All negative numbers"}
]

for i, test in enumerate(test_cases, 1):
    nums = test["nums"]
    expected = test["expected"]
    actual = solution.max_product(nums)
    assert actual == expected, f"Test {i} ({test['description']}) failed. Expected: {expected}, but got: {actual}"

print("All tests passed!")