"""
https://leetcode.com/problems/subarray-sum-equals-k/description/

Subarray Sum Equals K
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2
 
Constraints:
1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
"""

class Solution:
    def subarray_sum_equals_k(self, nums: list[int], k: int) -> int:
        """
        We create a hashmap to store all the prefixes that we have seen while
        iterating through our input array.
        Since sub-arrays must be contiguous, the prefixes that we store in our hashmap
        (as keys) will be the sum of elements to that point, and the value will be the
        number of times we have encountered them.
        """
        # Declare our result, and initialize to 0
        res = 0

        # Declare our hashmap and add 0 as a prefix
        prefixs_seen = {}
        prefixs_seen[0] = 1

        # Declare our sum and initialize to 0
        cur_sum = 0

        # Iterate through our array
        for num in nums:
            # Add the current element to the growing sum
            cur_sum += num
            # Calculate the value of the prefix we would have to get rid of in order to get k as a subarray of our current position
            # This is sum - k = the difference (aka what we need to get rid of to have k)
            difference = cur_sum - k
            # Check if that value is in our hash map
            if difference in prefixs_seen:
            # If it is, add the value of it to res
                res += prefixs_seen[difference]

            # Add the current sum as a prefix to our hashmap, or increment it
            prefixs_seen[cur_sum] = prefixs_seen.get(cur_sum, 0) + 1

        return res

solution = Solution()

test_cases = [
    {"nums": [1, 1, 1], "k": 2, "expected": 2, "description": "Example from problem statement"},
    {"nums": [1, 2, 3], "k": 3, "expected": 2, "description": "Example from problem statement"},
    {"nums": [5], "k": 5, "expected": 1, "description": "Single element matching k"},
    {"nums": [3, 4, -7, 1, 3, 3, 1, -4], "k": 7, "expected": 4, "description": "Array with negative numbers"},
    {"nums": [0, 0, 0, 0], "k": 0, "expected": 10, "description": "Array with zeros (all possible subarrays)"},
    {"nums": [1, 2, 3, 4], "k": 11, "expected": 0, "description": "No matching subarrays"}
]

for i, test in enumerate(test_cases, 1):
    nums = test["nums"]
    k = test["k"]
    expected = test["expected"]
    actual = solution.subarray_sum_equals_k(nums, k)
    assert actual == expected, f"Test {i} ({test['description']}) failed. Expected: {expected}, but got: {actual}"

print("All tests passed!")