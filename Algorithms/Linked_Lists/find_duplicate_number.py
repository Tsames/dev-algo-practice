"""
https://leetcode.com/problems/find-the-duplicate-number/description/

287. Find the Duplicate Number
Given an array of integers nums containing n + 1 integers where each integer is in the
range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and using only constant
extra space.

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3

Example 3:
Input: nums = [3,3,3,3,3]
Output: 3

Constraints:
1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which
appears two or more times.

Follow up:
How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem in linear runtime complexity?
"""

class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        """
        Problem Exploration:
        ____________________
        The restriction that we cannot modify our input array eliminates the
        potential solution of sorting and comparing adjacent numbers to find our
        duplicate.

        The restriction that we must complete our algorithm with constant extra space
        means we cannot use a hash map or set to check the occurrence count of
        elements of while we iterate over our input array.

        A brute force solution we could use would be to use a two pointer approach. In
        this approach we would loop through each element to the right of our left
        pointer element and compare, if we ever found two elements that were the same
        we could return that element since we know there is only a single duplicate.
        But this would be an O(n^2) solution.

        So where do we go from here?
        The problem gives us oddly specific conditions.
        First of all our array of length n + 1 contains all the integers from 1 to n
        with one integer in that range occurring exactly twice and the others occurring
        exactly once.
        So while we don't know the ordering of the numbers we know exactly which
        numbers are in our list with the exception of one.

        Solution:
        _________

        This ends up being a linked list cycle problem where we apply Floyd's algorithm
        to find the cycle.

        Let's elaborate: The value of the list indicates what index to check next. So
        if we have the following:

            [3,2,3,1]
            We would start at index 0: which has a value of 3
            So we check index 3: which has a value of 1
            So we check index 1: which has a value of 2
            So we check index 2: which has a value of 3.

        This forms a linked list cycle. The beginning of the cycle is the return value
        that we are looking for.

        The first portion of the algorithm uses a slow and a fast pointer. We iterate
        with each pointer until they intersect.

        The second portion of the algorithm is that we declare a second slow pointer.
        We then push both slow pointers along until they meet. They will meet at the
        beginning of the cycle of the linked list.

        Very tricky problem to even recognize that it's a linked list cycle problem and
        then apply a less intuitive and a bit of an arcane algorithm.
        """
        slow, fast = 0, 0
        # Find where the two pointers intersect
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Declare the second slow pointer
        slow2 = 0
        # Push both slow pointers along until they meet, return the element at that index.
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow

solution = Solution()

# Test case 1: Example from problem statement
expected = 2
actual = solution.findDuplicate([1, 3, 4, 2, 2])
assert actual == expected, f"Test one failed. Expected: {expected}, but got: {actual}"

# Test case 2: Example from problem statement
expected = 3
actual = solution.findDuplicate([3, 1, 3, 4, 2])
assert actual == expected, f"Test two failed. Expected: {expected}, but got: {actual}"

# Test case 3: Example from problem statement - all numbers are the same
expected = 3
actual = solution.findDuplicate([3, 3, 3, 3, 3])
assert actual == expected, f"Test three failed. Expected: {expected}, but got: {actual}"

# Test case 4: Larger array
expected = 5
actual = solution.findDuplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 5])
assert actual == expected, f"Test four failed. Expected: {expected}, but got: {actual}"

# Test case 5: Duplicate is the smallest value
expected = 1
actual = solution.findDuplicate([1, 1, 2, 3, 4])
assert actual == expected, f"Test five failed. Expected: {expected}, but got: {actual}"

# Test case 6: Duplicate is the largest valid value
expected = 4
actual = solution.findDuplicate([1, 2, 3, 4, 4])
assert actual == expected, f"Test six failed. Expected: {expected}, but got: {actual}"

print("All tests passed!")