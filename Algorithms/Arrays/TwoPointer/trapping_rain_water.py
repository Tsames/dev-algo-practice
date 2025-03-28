"""
https://neetcode.io/problems/trapping-rain-water
https://leetcode.com/problems/trapping-rain-water/description/

42. Trapping Rain Water
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:
n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
"""

class Solution:
    def trap(self, heights: list[int]) -> int:


# Tests for trapping_rain_water.py
solution = Solution()

# Test 1: Example from problem statement
heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
expected = 6
actual = solution.trap(heights)
assert actual == expected, f"Test 1 failed. Expected: {expected}, but got: {actual}"

# Test 2: Example from problem statement
heights = [4, 2, 0, 3, 2, 5]
expected = 9
actual = solution.trap(heights)
assert actual == expected, f"Test 2 failed. Expected: {expected}, but got: {actual}"

# Test 4: Single element
heights = [5]
expected = 0
actual = solution.trap(heights)
assert actual == expected, f"Test 4 failed. Expected: {expected}, but got: {actual}"

# Test 5: No trapped water (ascending)
heights = [1, 2, 3, 4, 5]
expected = 0
actual = solution.trap(heights)
assert actual == expected, f"Test 5 failed. Expected: {expected}, but got: {actual}"

# Test 6: No trapped water (descending)
heights = [5, 4, 3, 2, 1]
expected = 0
actual = solution.trap(heights)
assert actual == expected, f"Test 6 failed. Expected: {expected}, but got: {actual}"

# Test 7: Valley pattern
heights = [5, 1, 5]
expected = 4
actual = solution.trap(heights)
assert actual == expected, f"Test 7 failed. Expected: {expected}, but got: {actual}"

# Test 8: Complex pattern
heights = [5, 2, 1, 2, 1, 5]
expected = 14
actual = solution.trap(heights)
assert actual == expected, f"Test 8 failed. Expected: {expected}, but got: {actual}"

print("All tests passed!")