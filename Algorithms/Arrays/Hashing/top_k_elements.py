"""
https://neetcode.io/problems/top-k-elements-in-list

Top K Elements in List
Given an integer array nums and an integer k, return the k most frequent elements within the array.
The test cases are generated such that the answer is always unique.
You may return the output in any order.

Example 1:
Input: nums = [1,2,2,3,3,3], k = 2
Output: [2,3]

Example 2:
Input: nums = [7,7], k = 1
Output: [7]

Constraints:
1 <= nums.length <= 10^4.
-1000 <= nums[i] <= 1000
1 <= k <= number of distinct elements in nums.
"""
from collections import Counter

class Solution:
    def topKElements(self, nums: list[int], k: int) -> int:
        """ 
        Using python's counter object (fancy hashmap), count the number of times a given value occur in our input array.
        Then get the k most common elements as a list of tuples using counter's most_common method.
        Sort tuples of (value in list, number of times it occurs) based on index one's value (the number of times it occured).
        Place the first k values in our output array
        """
        res = []
        # O(n) for the counter object
        # O (n log n) for the most_common method
        # So this would simplify to O(n + (n * log n)) -> O(n * log n)
        counter = Counter(nums).most_common(k)
        return [pair[0] for pair in counter]

    def fastertopKElements(self, nums: list[int], k: int) -> int:
        '''
        The idea here is that we could improve extracting the keys with the most frequent counts from our hashmap.
        We assemble a list of lists of length equal to nums + 1.
        Each index represents that number appeared the index number frequently (thats why we need the +1, because the 0th index would represent a number appearing 0 times).
        So for example, if 6 was in the nested list at index 2, then we know 6 appeared twice in nums.

        So first we iterate through nums, counting each numbers frequency with a hashmap.
        Next we iterate through the key, value pairs appending the number to the nested list at the index that represents its frequency.

        Finally, we iterate backwards through our list k number of times, filling our result list with each iteration.
        This is O(n + n + n) -> O(3n) -> O(n) time complexity.
        '''
        counter = {}
        # O(n + 1) -> O(n) to create freq
        freq = [[] for i in range(len(nums) + 1)]

        # O(n) to fill up counter
        for n in nums:
            counter[n] = 1 + counter.get(n, 0)

        # O(n) to append keys at freq[value] for all (key, value) pairs in freq
        for num, count in counter.items():
            freq[count].append(num)

        # O(k) to fill up res
        res = []
        for i in reversed(range(len(freq))):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

solution = Solution()
assert solution.topKElements([1,2,2,3,3,3], 2) == [3,2], "Test one failed."
assert solution.topKElements([7,7], 1) == [7], f"Test two failed."

assert solution.fastertopKElements([1,2,2,3,3,3], 2) == [2,3], "Test three failed."
assert solution.fastertopKElements([7,7], 1) == [7], "Test four failed."
print("All tests passed!")
