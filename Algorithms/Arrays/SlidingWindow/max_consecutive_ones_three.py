'''
https://leetcode.com/problems/max-consecutive-ones-iii/description/

1004. Max Consecutive Ones III
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Constraints:
1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length
'''

class Solution:
    def longestOnes(self, nums, k):
        left = 0
        res = 0
        for right  in range(len(nums)):

            if nums[right] == 0:
                k -= 1

            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1

            res = max(res, right - left + 1)

        return res


solution = Solution()
assert solution.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2) == 6, "Test one failed."
assert solution.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2) == 6, "Test two failed."
assert solution.longestOnes( [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3) == 10, "Test three failed."
