"""
https://leetcode.com/problems/find-the-duplicate-number/description/

287. Find the Duplicate Number
Given an array of integers nums containing n + 1 integers where each integer is in the
range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and using only constant
extra space.

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3

Example 3:
Input: nums = [3,3,3,3,3]
Output: 3

Constraints:
1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which
appears two or more times.

Follow up:
How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem in linear runtime complexity?
"""

class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        """

        """


solution = Solution()

# Test case 1: Example from problem statement
expected = 2
actual = solution.findDuplicate([1,3,4,2,2])
assert actual == expected, f"Test one failed. Expected: {expected}, but got: {actual}"

# Test case 2: Example from problem statement
expected = 3
actual = solution.findDuplicate([3,1,3,4,2])
assert actual == expected, f"Test two failed. Expected: {expected}, but got: {actual}"

# Test case 3: Example from problem statement - all numbers are the same
expected = 3
actual = solution.findDuplicate([3,3,3,3,3])
assert actual == expected, f"Test three failed. Expected: {expected}, but got: {actual}"

# Test case 4: Larger array
expected = 5
actual = solution.findDuplicate([1,2,3,4,5,6,7,8,9,5])
assert actual == expected, f"Test four failed. Expected: {expected}, but got: {actual}"

# Test case 5: Duplicate is the smallest value
expected = 1
actual = solution.findDuplicate([1,1,2,3,4])
assert actual == expected, f"Test five failed. Expected: {expected}, but got: {actual}"

# Test case 6: Duplicate is the largest valid value
expected = 4
actual = solution.findDuplicate([1,2,3,4,4])
assert actual == expected, f"Test six failed. Expected: {expected}, but got: {actual}"

print("All tests passed!")