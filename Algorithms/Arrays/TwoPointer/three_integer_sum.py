"""
https://neetcode.io/problems/three-integer-sum

Three Integer Sum
Given an integer array nums,
return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k]
== 0,
and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the
triplets in any order.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:
3 <= nums.length <= 1000
-10^5 <= nums[i] <= 10^5
"""

"""
Plan:

Key observation here is that we can convert this problem into a two integer sum problem.
Setting our first pointer to the 0th index, we then set our next two pointers to the 
1st index
and the last index. We are now trying to find two numbers that when added to the first 
pointer make zero.

To make this work though, we need to sort the list first.
We also need to be wary of adding duplicates to our results array.

There are two cases in which we could stumble upon a duplicate:
1. When moving our leftmost pointer
2. When moving our two pointer pointers (in the case of our implementation only the 
left_pointer)
"""


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        for i, v in enumerate(nums):
            # If we come accross a duplicate value, continue
            if i > 0 and v == nums[i - 1]:
                continue

            # Otherwise, proceed with two pointer solution
            l, r = i + 1, len(nums) - 1
            while l < r:
                sum = v + nums[l] + nums[r]
                if sum < 0:
                    l += 1
                elif sum > 0:
                    r -= 1
                else:
                    res.append([v, nums[l], nums[r]])
                    l += 1
                    while nums[l - 1] == nums[l] and l < r:
                        l += 1

        return res


solution = Solution()

# Test case 1: Example from problem statement
nums = [-1, 0, 1, 2, -1, -4]
expected = [[-1, -1, 2], [-1, 0, 1]]
actual = solution.threeSum(nums)
# Sort the inner lists for comparison
actual_sorted = [sorted(triplet) for triplet in actual]
expected_sorted = [sorted(triplet) for triplet in expected]
assert sorted(actual_sorted) == sorted(expected_sorted), f"Test 1 failed. Expected: {expected}, but got: {actual}"

# Test case 2: Example from problem statement
nums = [0, 1, 1]
expected = []
actual = solution.threeSum(nums)
assert actual == expected, f"Test 2 failed. Expected: {expected}, but got: {actual}"

# Test case 3: Example from problem statement
nums = [0, 0, 0]
expected = [[0, 0, 0]]
actual = solution.threeSum(nums)
assert actual == expected, f"Test 3 failed. Expected: {expected}, but got: {actual}"

# Test case 4: Multiple zeros
nums = [0, 0, 0, 0]
expected = [[0, 0, 0]]
actual = solution.threeSum(nums)
assert actual == expected, f"Test 4 failed. Expected: {expected}, but got: {actual}"

# Test case 5: Multiple triplets
nums = [-2, -1, 0, 1, 2, 3]
expected = [[-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]
actual = solution.threeSum(nums)
# Sort for comparison
actual_sorted = [sorted(triplet) for triplet in actual]
expected_sorted = [sorted(triplet) for triplet in expected]
assert sorted(actual_sorted) == sorted(expected_sorted), f"Test 5 failed. Expected: {expected}, but got: {actual}"

# Test case 6: Only negative numbers
nums = [-3, -2, -1]
expected = []
actual = solution.threeSum(nums)
assert actual == expected, f"Test 6 failed. Expected: {expected}, but got: {actual}"

print("All tests passed!")