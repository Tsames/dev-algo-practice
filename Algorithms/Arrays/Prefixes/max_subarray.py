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
    def maxSubArrayBrute(self, nums: list[int]) -> int:
        res = float("-inf")

        for i in range(len(nums)):
            cur_sum = 0
            for j in range(i, len(nums)):
                cur_sum += nums[j]
                res = max(res, cur_sum)

        return res

    def maxSubArray(self, nums: list[int]) -> int:
        """
        The whole idea here is that if we ever encounter a negative prefix, we should
        reset the beginning of the subarray we are considering to a new num.
        This makes sense because negative prefixes (cur_sum to that point) don't help us
        build a bigger subarray.
        """
        res = float("-inf")
        cur_sum = 0

        for n in nums:
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += n
            res = max(res, cur_sum)

        return res

solution = Solution()

test_cases = [
    {"nums": [-2, 1, -3, 4, -1, 2, 1, -5, 4], "expected": 6, "description": "Mix of positive and negative numbers"},
    {"nums": [1], "expected": 1, "description": "Single element array"},
    {"nums": [5, 4, -1, 7, 8], "expected": 23, "description": "Mostly positive numbers"},
    {"nums": [-5, -4, -1, -7, -8], "expected": -1, "description": "All negative numbers"}
]

# Test the optimized solution
for i, test in enumerate(test_cases, 1):
    nums = test["nums"]
    expected = test["expected"]
    actual = solution.maxSubArray(nums)
    assert actual == expected, f"Test {i} ({test['description']}) failed. Expected: {expected}, but got: {actual}"

# Test the brute force solution
for i, test in enumerate(test_cases, 1):
    nums = test["nums"]
    expected = test["expected"]
    actual = solution.maxSubArrayBrute(nums)
    assert actual == expected, f"Test {i} ({test['description']}) with brute force failed. Expected: {expected}, but got: {actual}"

print("All tests passed!")