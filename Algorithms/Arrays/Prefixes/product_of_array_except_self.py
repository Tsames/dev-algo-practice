"""
https://leetcode.com/problems/product-of-array-except-self/description/

Product of Array Except Self
Given an integer array nums, return an array answer such that answer[i] is equal to the
product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division
operation.

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

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array
does not count as extra space for space complexity analysis.)
"""

class Solution:
    def product_except_self_with_extra_space(self, nums: list[int]) -> list[int]:
        """
        We want to find the product of all element of the input array excluding the
        current index.
        To do this, we need two numbers.
        One, we need the product of all elements in the input array before the current
        index.
        Two, we need the product of all elements in the input array after the current
        index.
        We multiply them together and, wahla.

        To get the two products we need, we iterate through our input array twice.
        We store the prefix and suffix product in separate arrays.
        Then we iterate through a third time and do our calculations, adding the result to our output array.
        """
        prefixes = [0] * len(nums)
        suffixes = [0] * len(nums)

        # Calculate our Prefixes
        prefix_product = 1
        for i in range(len(nums)):
            prefixes[i] = prefix_product
            prefix_product *= nums[i]

        # Calculate Suffixes
        suffix_product = 1
        for j in reversed(range(len(nums))):
            suffixes[j] = suffix_product
            suffix_product *= nums[j]

        res = []
        for k in range(len(nums)):
            res.append(prefixes[k] * suffixes[k])

        return res

solution = Solution()

test_cases = [
    {"nums": [1, 2, 3, 4], "expected": [24, 12, 8, 6],
     "description": "Example from problem statement"},
    {"nums": [-1, 1, 0, -3, 3], "expected": [0, 0, 9, 0, 0],
     "description": "Array with zero"},
    {"nums": [1, 1], "expected": [1, 1], "description": "Minimum length array"},
    {"nums": [2, 3, 4, 5], "expected": [60, 40, 30, 24],
     "description": "All positive integers"},
    {"nums": [-2, -3, -4], "expected": [12, 8, 6],
     "description": "All negative integers"},
    {"nums": [-1, 1, -1, 1], "expected": [-1, 1, -1, 1],
     "description": "Alternating signs"},
    {"nums": [0, 0, 0, 0], "expected": [0, 0, 0, 0], "description": "All zeros"},
    {"nums": [10, 3, 5, 6, 2], "expected": [180, 600, 360, 300, 900],
     "description": "Larger numbers"},
    {"nums": [0, 1, 2, 0], "expected": [0, 0, 0, 0], "description": "Multiple zeros"}
]

for i, test in enumerate(test_cases, 1):
    nums = test["nums"]
    expected = test["expected"]
    actual = solution.product_except_self_with_extra_space(nums)
    assert actual == expected, (f"Test {i} ({test['description']}) failed. Expected: "
                                f"{expected}, but got: {actual}")

print("All tests passed!")
