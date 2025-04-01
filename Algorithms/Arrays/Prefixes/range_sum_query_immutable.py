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

test_cases = [
    {
        "nums": [-2, 0, 3, -5, 2, -1],
        "queries": [(0, 2, 1), (2, 5, -1), (0, 5, -3), (3, 3, -5)],
        "description": "Example from problem statement"
    },
    {
        "nums": [1, 2, 3, 4, 5],
        "queries": [(1, 3, 9), (0, 4, 15), (2, 4, 12)],
        "description": "All positive integers"
    },
    {
        "nums": [-1, -2, -3, -4, -5],
        "queries": [(0, 2, -6), (1, 3, -9), (0, 4, -15)],
        "description": "All negative integers"
    },
    {
        "nums": [10],
        "queries": [(0, 0, 10)],
        "description": "Single element array"
    },
    {
        "nums": [5, 0, 7, 0, 8],
        "queries": [(0, 4, 20), (1, 3, 7), (1, 1, 0)],
        "description": "Array with zeros"
    }
]

for i, test in enumerate(test_cases, 1):
    nums = test["nums"]
    queries = test["queries"]
    description = test["description"]

    num_array = NumArray(nums)

    for j, (left, right, expected) in enumerate(queries, 1):
        actual = num_array.sum_range(left, right)
        assert actual == expected, f"Test {i}.{j} ({description}) failed. Range [{left}, {right}] - Expected: {expected}, but got: {actual}"

print("All tests passed!")