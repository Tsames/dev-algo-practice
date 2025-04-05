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
        """
        If we want to find a pivot we need to know that the first n elements total the same number as the last m
        elements.
        One way that we could do this is by computing a prefix and a suffix array.
        The prefix array would hold the sum of all elements occurring before the current element.
        The suffix array would hold the sum of all elements occurring after the current element.

        We would then iterate through our input array, comparing that same index in our prefix and suffix array.
        The first element we find that has the same value in both prefix and suffix arrays would be what we return.

        This would be an O(n) time complexity and O(n) space complexity solution
        """
        prefixes, suffixes = [0] * len(nums), [0] * len(nums)
        sum_curr = 0
        for i in range(len(nums)):
            prefixes[i] = sum_curr
            sum_curr += nums[i]

        sum_curr = 0
        for j in reversed(range(len(nums))):
            suffixes[j] = sum_curr
            sum_curr += nums[j]

        for k in range(len(nums)):
            if prefixes[k] == suffixes[k]:
                return k

        return -1

    def pivot_index_faster(self, nums: list[int]) -> int:
        total = sum(nums)

        prefix_sum = 0
        for i in range((len(nums))):
            suffix_sum = total - nums[i] - prefix_sum
            if prefix_sum == suffix_sum:
                return i
            prefix_sum += nums[i]
        return -1

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
    {"nums": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 45], "expected": 9, "description": "Pivot index at the end"}
]

for i, test in enumerate(test_cases, 1):
    nums = test["nums"]
    expected = test["expected"]
    actual = solution.pivot_index(nums)
    assert actual == expected, f"Test {i} ({test['description']}) failed. Expected: {expected}, but got: {actual}"

for i, test in enumerate(test_cases, 1):
    nums = test["nums"]
    expected = test["expected"]
    actual = solution.pivot_index_faster(nums)
    assert actual == expected, (f"Test {i} ({test['description']}) for pivot index faster failed. Expected:"
                                f" {expected},ut got: {actual}")

print("All tests passed!")