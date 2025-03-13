"""
https://leetcode.com/problems/minimum-positive-sum-subarray/description/?envType
=problem-list-v2&envId=sliding-window

Minimum Positive Sum Subarray
You are given an integer array nums and two integers l and r. Your task is to find the
minimum sum of a subarray whose size is between l and r (inclusive) and whose sum is
greater than 0.
Return the minimum sum of such a subarray. If no such subarray exists, return -1.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [3, -2, 1, 4], l = 2, r = 3
Output: 1
Explanation:
The subarrays of length between l = 2 and r = 3 where the sum is greater than 0 are:
[3, -2] with a sum of 1
[1, 4] with a sum of 5
[3, -2, 1] with a sum of 2
[-2, 1, 4] with a sum of 3
Out of these, the subarray [3, -2] has a sum of 1, which is the smallest positive sum.
Hence, the answer is 1.

Example 2:
Input: nums = [-2, 2, -3, 1], l = 2, r = 3
Output: -1
Explanation:

There is no subarray of length between l and r that has a sum greater than 0. So,
the answer is -1.

Example 3:
Input: nums = [1, 2, 3, 4], l = 2, r = 4
Output: 3
Explanation:
The subarray [1, 2] has a length of 2 and the minimum sum greater than 0. So,
the answer is 3.

Constraints:
1 <= nums.length <= 100
1 <= l <= r <= nums.length
-1000 <= nums[i] <= 1000
"""


class Solution:
    def minimumSumSubArray(self, nums, l, r):
        """
        Explore:
        -------

        Intuitively, we want to iterate through our given array, maintaining a window
        that will consider all possible subarray that are of size l <= s <= r where s
        is the size of our window.

        Lets looks at an example:
        [1, 2, 3, 4, 5] : l = 2 : r = 3

        We want our window to stretch to its maximum size right away.

            [1,2] -> [1,2,3]

        Next we would want our window to shrink down to it minimum size, moving its
        left end to the right.

            [2,3]

        Then we would again want to stretch the window to its maximum size.

            [2,3,4]

       We follow this pattern until the end. Once the left side of our window is far
       enough into our array that we can't form a big enough window, we would stop.

       Thus, a simplified version of the rule could be that our left pointer is less
       than the length of nums.

       Outline:
       --------

        Declare a res variable to keep track of the subarray with the minimum value.
        This variable should start at -1 since this is the value that should be
        returned if we can't find any subarrays that satisfy our conditions.
        Declare a minSum variable set to positive infinity.

        Declare a left pointer, left_pointer, and a right pointer, right_pointer,
        both set to 0.
        Declare a curSum variable, set to 0.

        Iterate while left is less than the length of nums:
            The size of our subarray is equal to right - left + 1 (since arrays are 0
            indexed)

            If our window is an acceptable size, the sum of the window is greater than
            0, and the sum of the window is less than previous windows, then
                Set res to the current window.


        """
        res = -1
        left_pointer, right_pointer = 0, 0
        minSum, curSum = float("inf"), 0

        while right_pointer < len(nums):
            while right_pointer < len(nums) and right_pointer - left_pointer + 1 < r:


            # Evaluate the window
            # if l <= size and size <= r and curSum >0 and curSum < minSum:
            #     res = nums[left_pointer:right_pointer + 1]
            #     minSum = curSum

solution = Solution()

# Test case 1
expected = 1
actual = solution.minimumSumSubArray([3, -2, 1, 4], 2, 3)
assert actual == expected, f"Test one failed. Expected: {expected}, but got: {actual}"

# Test case 2
expected = -1
actual = solution.minimumSumSubArray([-2, 2, -3, 1], 2, 3)
assert actual == expected, f"Test two failed. Expected: {expected}, but got: {actual}"

# Test case 3
expected = 3
actual = solution.minimumSumSubArray([1, 2, 3, 4], 2, 4)
assert actual == expected, f"Test three failed. Expected: {expected}, but got: {actual}"

print("All tests passed!")