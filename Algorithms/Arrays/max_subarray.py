"""
https://leetcode.com/problems/maximum-subarray/description/

Maximum Subarray
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 
Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
 
Follow up: If you have figured out the O(n) solution, try coding another solution using
the divide and conquer approach, which is more subtle.
"""

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        res = float("-inf")
        sum = 0

        l = r = 0
        while r < len(nums):
            sum += nums[r]
            res = max(res, sum)

            if sum < 0:
                sum = 0
                l += 1

            r += 1

        return res

solution = Solution()

# Test case 1: Mix of positive and negative numbers
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
expected = 6
actual = solution.maxSubArray(nums)
assert actual == expected, f"Test 1 failed. Expected: {expected}, but got: {actual}"

# Test case 2: Single element array
nums = [1]
expected = 1
actual = solution.maxSubArray(nums)
assert actual == expected, f"Test 2 failed. Expected: {expected}, but got: {actual}"

# Test case 3: Mostly positive numbers
nums = [5, 4, -1, 7, 8]
expected = 23
actual = solution.maxSubArray(nums)
assert actual == expected, f"Test 3 failed. Expected: {expected}, but got: {actual}"

# Test case 4: All negative numbers
nums = [-5, -4, -1, -7, -8]
expected = -1
actual = solution.maxSubArray(nums)
assert actual == expected, f"Test 4 failed. Expected: {expected}, but got: {actual}"

print("All tests passed!")