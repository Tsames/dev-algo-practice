'''
https://leetcode.com/problems/subarray-sum-equals-k/description/

560. Subarray Sum Equals K
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
'''

class Solution:
    def subarray_sum_equals_k(self, nums: list[int], k: int) -> int:
        # Declare our result, and initialize to 0
        res = 0
        
        # Declare our hashmap and add 0 as a prefix
        prefixs_seen = {}
        prefixs_seen[0] = 1
        
        # Declare our sum and initialize to 0
        sum = 0
        
        # Iterate through our array
        for num in nums:
            # Add the current element to the growing sum
            sum += num
            # Calculate the value of the prefix we would have to get rid of in order to get k as a subarray of our current position
            # This is sum - k = the difference (aka what we need to get rid of to have k)
            difference = sum - k
            # Check if that value is in our hash map
            if difference in prefixs_seen:
            # If it is, add the value of it to res
                res += prefixs_seen[difference]
                
            # Add the current sum as a prefix to our hashmap, or increment it
            prefixs_seen[sum] = prefixs_seen.get(sum, 0) + 1
            
        return res
        
solution = Solution()
assert solution.subarray_sum_equals_k([1,1,1], 2) == 2, "Test Case 1 Failed"
assert solution.subarray_sum_equals_k([1,2,3], 3) == 2, "Test Case 2 Failed"