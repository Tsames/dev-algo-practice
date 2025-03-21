"""
https://neetcode.io/problems/longest-consecutive-sequence
https://leetcode.com/problems/longest-consecutive-sequence/description/

Longest Consecutive Sequence
Given an unsorted array of integers nums, return the length of the longest consecutive
elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore,
its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Example 3:
Input: nums = [1,0,1,2]
Output: 3

Constraints:
0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

class Solution:
    def longest_consecutive_sequence(self, nums: list[int]) -> int:
        """
        Our input array is unsorted, which makes it trickier to know if elements we
        encounter while iterating through our array are continuing an existing
        consecutive sequence or are on an island.

        Since we are required to find a solution that has O(n) time complexity we are
        unable to sort our input array for the easy way out.

        Any given number is part of a sequence if the number that comes before it or
        after it exists in our input array. We could create a hashmap and use the
        values to represent the length of sequence so far and the keys to represent the
        values.
        This has the problem of updating values for the entire sequence since a new key
        could connect previously non-consecutive sequences.
        Another problem is that its not clear where to look for the most up to date
        information of how long the sequence is. New numbers that are added to the
        sequence could be from multiple values.

        So, a hashmap can help us know if a number has already occurred in our input
        array, but it doesn't help us know how long that sequence might be.

        Maybe we can instead use a set.

        We can know if any given number is the start of a sequence by whether or not it has a left neighbor.
        If it has a left neighbor, we can count the length of the sequence using our
        set one by one.
        If it doesn't have a left neighbor, we just move on.
        """

        longest = 0
        all_nums = set(nums)

        for num in nums:
            # Check and see if the current number is the start of a sequence
            if (num - 1) in all_nums:
                continue

            # If it is the start of a new sequence (doesn't have a left neighbor),
            # then lets count how big the sequence is
            sequence_length = 1
            while (num + 1) in all_nums:
                sequence_length += 1
                num += 1
            longest = max(longest, sequence_length)

        return longest

solution = Solution()

# Test case 1: Example from problem statement
nums = [100, 4, 200, 1, 3, 2]
expected = 4
actual = solution.longest_consecutive_sequence(nums)
assert actual == expected, f"Test 1 failed. Expected: {expected}, but got: {actual}"

# Test case 2: Example from problem statement
nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
expected = 9
actual = solution.longest_consecutive_sequence(nums)
assert actual == expected, f"Test 2 failed. Expected: {expected}, but got: {actual}"

# Test case 3: Example from problem statement
nums = [1, 0, 1, 2]
expected = 3
actual = solution.longest_consecutive_sequence(nums)
assert actual == expected, f"Test 3 failed. Expected: {expected}, but got: {actual}"

# Test case 4: Single element
nums = [5]
expected = 1
actual = solution.longest_consecutive_sequence(nums)
assert actual == expected, f"Test 4 failed. Expected: {expected}, but got: {actual}"

# Test case 5: All elements are the same
nums = [2, 2, 2, 2]
expected = 1
actual = solution.longest_consecutive_sequence(nums)
assert actual == expected, f"Test 5 failed. Expected: {expected}, but got: {actual}"

# Test case 6: Large consecutive sequence
nums = [10, 5, 12, 3, 55, 30, 4, 11, 2]
expected = 4  # The sequence is [2, 3, 4, 5]
actual = solution.longest_consecutive_sequence(nums)
assert actual == expected, f"Test 6 failed. Expected: {expected}, but got: {actual}"

# Test case 7: Disjoint sequences
nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
expected = 10  # The sequence is [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
actual = solution.longest_consecutive_sequence(nums)
assert actual == expected, f"Test 7 failed. Expected: {expected}, but got: {actual}"

print("All tests passed!")
