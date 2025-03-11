"""
https://neetcode.io/problems/two-integer-sum-ii

Two Integer Sum II
Given an array of integers numbers that is sorted in non-decreasing order.
Return the indices (1-indexed) of two numbers, [index1, index2],
such that they add up to a given target number target and index1 < index2.
Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

There will always be exactly one valid solution.
Your solution must use O(1) additional space.

Example 1:
Input: numbers = [1,2,3,4], target = 3
Output: [1,2]
Explanation:
The sum of 1 and 2 is 3. Since we are assuming a 1-indexed array, index1 = 1, index2 = 2. We return [1, 2].

Constraints:
2 <= numbers.length <= 1000
-1000 <= numbers[i] <= 1000
-1000 <= target <= 1000
"""

"""
Plan:

Create a left pointer set to the beginning of the given list and
our right pointer to the end.

Within a while loop we add the numbers at each index together.

If the number is equal to the target, we return a new list with those indexes.
If the number is less than the target, we move the left pointer up one index.
If the number is greater than, we move the right pointer down one index.
"""

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left_pointer = 0
        right_pointer = len(numbers) - 1
        
        while left_pointer < right_pointer:            
            sum = numbers[left_pointer] + numbers[right_pointer]
            if sum == target:
                return [left_pointer + 1, right_pointer + 1]
            elif sum > target:
                right_pointer -= 1
            else:
                left_pointer += 1
        
        return None
    
solution = Solution()
assert solution.twoSum([1,2,3,4], 3) == [1,2]
assert solution.twoSum([2,3,4], 6) == [1,3]

