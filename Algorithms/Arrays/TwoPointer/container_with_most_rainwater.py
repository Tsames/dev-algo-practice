"""
https://neetcode.io/problems/max-water-container
https://leetcode.com/problems/container-with-most-water/description/

Container With Most Water
You are given an integer array heights where heights[i] represents the height of the
ith bar.
You may choose any two bars to form a container. Return the maximum amount of water a
container can store.

Example 1:
Input: height = [1,7,2,5,4,7,3,6]
Output: 36

Example 2:
Input: height = [2,2,2]
Output: 4

Constraints:
2 <= height.length <= 1000
0 <= height[i] <= 1000
"""


class Solution:
    def maxArea(self, height: list[int]) -> int:
        """
        We could solve this problem using a two pointer approach where we begin with
        our left pointer and right pointer at the beginning and end of our input array
        respectively.

        We iterate through our array while left pointer is less than our right pointer.
        At each iteration we calculate the area of water that could fit between the two heights.
        We do this by multiplying the distance between the two points (right pointer
        minus left pointer) and multiply that number by the smaller of the two heights.

        At each iteration we compare the area of those two heights with the max so far.

        Then we move our whichever pointer has a shorter height.
        if they are both the same height, then lets move our left pointer over.
        """

        res = 0
        left, right = 0, len(height) - 1

        while left < right:
            area = min(height[left], height[right]) * (right - left)
            res = max(res, area)

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return res


solution = Solution()

# Test case 1: Example from problem statement
heights = [1, 7, 2, 5, 4, 7, 3, 6]
expected = 36
actual = solution.maxArea(heights)
assert actual == expected, f"Test 1 failed. Expected: {expected}, but got: {actual}"

# Test case 2: Example from problem statement
heights = [2, 2, 2]
expected = 4
actual = solution.maxArea(heights)
assert actual == expected, f"Test 2 failed. Expected: {expected}, but got: {actual}"

# Test case 3: Minimum valid input
heights = [1, 1]
expected = 1
actual = solution.maxArea(heights)
assert actual == expected, f"Test 3 failed. Expected: {expected}, but got: {actual}"

# Test case 4: Ascending heights
heights = [1, 2, 3, 4, 5]
expected = 6
actual = solution.maxArea(heights)
assert actual == expected, f"Test 4 failed. Expected: {expected}, but got: {actual}"

# Test case 5: Descending heights
heights = [5, 4, 3, 2, 1]
expected = 6
actual = solution.maxArea(heights)
assert actual == expected, f"Test 5 failed. Expected: {expected}, but got: {actual}"

# Test case 6: Large differences in heights
heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
expected = 49
actual = solution.maxArea(heights)
assert actual == expected, f"Test 6 failed. Expected: {expected}, but got: {actual}"

# Test case 7: All zeros
heights = [0, 0, 0, 0]
expected = 0
actual = solution.maxArea(heights)
assert actual == expected, f"Test 7 failed. Expected: {expected}, but got: {actual}"

# Test case 8: Single high bar in the middle
heights = [1, 2, 10, 2, 1]
expected = 4
actual = solution.maxArea(heights)
assert actual == expected, f"Test 8 failed. Expected: {expected}, but got: {actual}"

print("All tests passed!")
