"""
https://leetcode.com/problems/find-pivot-index/description/

Find Pivot Index
Given an array of integers nums, calculate the pivot index of this array.
The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum
of all the numbers strictly to the index's right.
If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This
also applies to the right edge of the array.
Return the leftmost pivot index. If no such index exists, return -1.

Example 1:
Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11

Example 2:
Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.

Example 3:
Input: nums = [2,1,-1]
Output: 0
Explanation:
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0

Constraints:
1 <= nums.length <= 104
-1000 <= nums[i] <= 1000

Note: This question is the same as 1991: https://leetcode.com/problems/find-the-middle-index-in-array/k
"""
class Solution:
    def pivot_index(self, nums: list[int]) -> int:


solution = Solution()

test_cases = [
    {"nums": [1, 7, 3, 6, 5, 6], "expected": 3, "description": "Example from problem statement"},
    {"nums": [1, 2, 3], "expected": -1, "description": "No pivot index"},
    {"nums": [2, 1, -1], "expected": 0, "description": "Pivot index at the start"},
    {"nums": [0, 0, 0, 0], "expected": 0, "description": "All zeros"},
    {"nums": [1, -1, 1, -1, 1, -1, 1], "expected": 0, "description": "Alternating signs"},
    {"nums": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "expected": -1, "description": "No pivot index in an "
                                                                             "non-negative ascending sequence"},
    {"nums": [-1, -1, -1, 0, 1, 1], "expected": 0, "description": "Pivot index at the start with negative numbers"},
    {"nums": [1, 2, 3, 4, 5, 6, 7, 8, 9, -45], "expected": 9, "description": "Pivot index at the end"}
]

for i, test in enumerate(test_cases, 1):
    nums = test["nums"]
    expected = test["expected"]
    actual = solution.pivot_index(nums)
    assert actual == expected, f"Test {i} ({test['description']}) failed. Expected: {expected}, but got: {actual}"

print("All tests passed!")
