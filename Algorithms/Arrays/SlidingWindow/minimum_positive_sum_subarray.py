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
        minSum = float('inf')
        for i in range(l, r + 1):
            currSum = 0

            for j in range(i):
                currSum += nums[j]
            if currSum > 0:
                minSum = min(minSum, currSum)

            low, high = 0, i

            while high < len(nums):
                currSum -= nums[low]
                currSum += nums[high]

                low += 1
                high += 1

                if currSum > 0:
                    minSum = min(minSum, currSum)

        if minSum == float('inf'):
            return -1
        return minSum


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