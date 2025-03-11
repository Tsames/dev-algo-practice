'''
https://leetcode.com/problems/product-of-array-except-self/description/
https://neetcode.io/problems/products-of-array-discluding-self

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
'''

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix_product, postfix_product = 1, 1
        prefixes, postfixes = [1] * len(nums), [1] * len(nums)

        for i in range(len(nums)):
            prefix_product *= nums[i]
            prefixes[i] = prefix_product

        for i in reversed(range(len(nums))):
            postfix_product *= nums[i]
            postfixes[i] = postfix_product

        res = []
        for i in range(len(nums)):
            prefix = 1 if i == 0 else prefixes[i - 1]
            postfix = 1 if i == (len(nums) - 1) else postfixes[i + 1]
            res.append(prefix * postfix)

        return res

    def productExceptSelfLessSpace(self, nums: list[int]) -> list[int]:
        res = [1] * len(nums)
        product = 1

        for i in range(len(nums)):
            res[i] = product
            product *= nums[i]

        product = 1
        for j in reversed(range(len(nums))):
            res[j] = res[j] * product
            product *= nums[j]

        return res

solution = Solution()

# Test case 1
expected = [24, 12, 8, 6]
actual = solution.productExceptSelf([1, 2, 3, 4])
assert actual == expected, f"Test one failed. Expected: {expected}, but got: {actual}"

# Test case 2
expected = [0, 0, 9, 0, 0]
actual = solution.productExceptSelf([-1, 1, 0, -3, 3])
assert actual == expected, f"Test two failed. Expected: {expected}, but got: {actual}"

# Test case 3
expected = [0, 0, 0, 0, 0]
actual = solution.productExceptSelf([0, 9, 9, 9, 0])
assert actual == expected, f"Test three failed. Expected: {expected}, but got: {actual}"

# Test case 4
expected = [120, 40, 30, 24, 60]
actual = solution.productExceptSelf([-1, -3, -4, -5, -2])
assert actual == expected, f"Test four failed. Expected: {expected}, but got: {actual}"

# Test case 5
expected = [24, 12, 8, 6]
actual = solution.productExceptSelfLessSpace([1, 2, 3, 4])
assert actual == expected, f"Test one failed. Expected: {expected}, but got: {actual}"

# Test case 6
expected = [0, 0, 9, 0, 0]
actual = solution.productExceptSelfLessSpace([-1, 1, 0, -3, 3])
assert actual == expected, f"Test two failed. Expected: {expected}, but got: {actual}"

# Test case 7
expected = [0, 0, 0, 0, 0]
actual = solution.productExceptSelfLessSpace([0, 9, 9, 9, 0])
assert actual == expected, f"Test three failed. Expected: {expected}, but got: {actual}"

# Test case 8
expected = [120, 40, 30, 24, 60]
actual = solution.productExceptSelfLessSpace([-1, -3, -4, -5, -2])
assert actual == expected, f"Test four failed. Expected: {expected}, but got: {actual}"

print("All tests passed!")
