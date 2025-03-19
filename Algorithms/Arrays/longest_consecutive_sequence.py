"""
https://neetcode.io/problems/longest-consecutive-sequence
https://leetcode.com/problems/longest-consecutive-sequence/description/

Longest Consecutive Sequence
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore,
its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Example 3:
Input: nums = [1,0,1,2]
Output: 3

Constraints:
0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

class Solution:
    def longest_consecutive_sequence(self, nums: list[int]) -> int:


solution = Solution()

# Test case 1: Example from problem statement
nums = [100, 4, 200, 1, 3, 2]
expected = 4
actual = solution.longest_consecutive_sequence(nums)
assert actual == expected, f"Test 1 failed. Expected: {expected}, but got: {actual}"

# Test case 2: Example from problem statement
nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
expected = 9
actual = solution.longest_consecutive_sequence(nums)
assert actual == expected, f"Test 2 failed. Expected: {expected}, but got: {actual}"

# Test case 3: Example from problem statement
nums = [1, 0, 1, 2]
expected = 3
actual = solution.longest_consecutive_sequence(nums)
assert actual == expected, f"Test 3 failed. Expected: {expected}, but got: {actual}"

# Test case 4: Empty array
nums = []
expected = 0
actual = solution.longest_consecutive_sequence(nums)
assert actual == expected, f"Test 4 failed. Expected: {expected}, but got: {actual}"

# Test case 5: Single element
nums = [5]
expected = 1
actual = solution.longest_consecutive_sequence(nums)
assert actual == expected, f"Test 5 failed. Expected: {expected}, but got: {actual}"

# Test case 6: All elements are the same
nums = [2, 2, 2, 2]
expected = 1
actual = solution.longest_consecutive_sequence(nums)
assert actual == expected, f"Test 6 failed. Expected: {expected}, but got: {actual}"

# Test case 7: Large consecutive sequence
nums = [10, 5, 12, 3, 55, 30, 4, 11, 2]
expected = 4  # The sequence is [2, 3, 4, 5]
actual = solution.longest_consecutive_sequence(nums)
assert actual == expected, f"Test 7 failed. Expected: {expected}, but got: {actual}"

# Test case 8: Negative numbers
nums = [-1, -3, -2, 0, 1, 2]
expected = 4  # The sequence is [-3, -2, -1, 0]
actual = solution.longest_consecutive_sequence(nums)
assert actual == expected, f"Test 8 failed. Expected: {expected}, but got: {actual}"

# Test case 9: Large input (stress test)
nums = list(range(-1000, 1001))
expected = 2001  # The sequence is [-1000, -999, ..., 999, 1000]
actual = solution.longest_consecutive_sequence(nums)
assert actual == expected, f"Test 9 failed. Expected: {expected}, but got: {actual}"

# Test case 10: Disjoint sequences
nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
expected = 10  # The sequence is [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
actual = solution.longest_consecutive_sequence(nums)
assert actual == expected, f"Test 10 failed. Expected: {expected}, but got: {actual}"

print("All tests passed!")

