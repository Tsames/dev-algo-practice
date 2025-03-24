"""
https://leetcode.com/problems/range-sum-query-immutable/description/

Range Sum Query - Immutable
Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive
where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between
indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

Example 1:
Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]

Explanation
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3

Constraints:
1 <= nums.length <= 104
-105 <= nums[i] <= 105
0 <= left <= right < nums.length
At most 104 calls will be made to sumRange.
"""
class NumArray:

    def __init__(self, nums):
        self.prefixes = []
        prefix_sum = 0
        for n in nums:
            prefix_sum += n
            self.prefixes.append(prefix_sum)

    def sum_range(self, left, right):
        right_sum = self.prefixes[right]
        left_sum = self.prefixes[left - 1] if left > 0 else 0
        return right_sum - left_sum

nums = [-2, 0, 3, -5, 2, -1]
num_array = NumArray(nums)

# Test case 1: Example from problem statement
left, right = 0, 2
expected = 1  # (-2) + 0 + 3 = 1
actual = num_array.sum_range(left, right)
assert actual == expected, f"Test 1 failed. Expected: {expected}, but got: {actual}"

# Test case 2: Example from problem statement
left, right = 2, 5
expected = -1  # 3 + (-5) + 2 + (-1) = -1
actual = num_array.sum_range(left, right)
assert actual == expected, f"Test 2 failed. Expected: {expected}, but got: {actual}"

# Test case 3: Example from problem statement
left, right = 0, 5
expected = -3  # (-2) + 0 + 3 + (-5) + 2 + (-1) = -3
actual = num_array.sum_range(left, right)
assert actual == expected, f"Test 3 failed. Expected: {expected}, but got: {actual}"

# Test case 4: Single element range
left, right = 3, 3
expected = -5  # Just the element at index 3
actual = num_array.sum_range(left, right)
assert actual == expected, f"Test 4 failed. Expected: {expected}, but got: {actual}"

# Test case 5: Different array
nums = [1, 2, 3, 4, 5]
num_array = NumArray(nums)
left, right = 1, 3
expected = 9  # 2 + 3 + 4 = 9
actual = num_array.sum_range(left, right)
assert actual == expected, f"Test 5 failed. Expected: {expected}, but got: {actual}"

print("All tests passed!")