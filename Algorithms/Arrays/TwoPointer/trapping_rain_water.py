"""
https://neetcode.io/problems/trapping-rain-water
https://leetcode.com/problems/trapping-rain-water/description/

42. Trapping Rain Water
Given n non-negative integers representing an elevation map where the width of each bar
is 1, compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,
1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

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
        """
        Initial Thoughts

        We only trap rainwater when there is a valley between two taller heights (I
        will call these two heights bookends).
        If there is an ascending or descending pattern of heights, then we don't trap any
        rainwater.

        So we need to find and calculate the area of the valleys in our input array and
        then add them all up together to get our output. By a valley, I mean a pattern of
        heights of at least length three where the middle height is at least shorter than
        the bookend points by 1.

        We could proceed along the input array, everytime we find a valley, we add the
        valleys' area to the total. Then we look for our next valley.

        But we also need a way to calculate our valley. We need to keep track of the
        area of our valley as we iterate through it.

        So we declare a left and right pointer.
        We walk our right pointer out from our left pointer.

            If we run into a height that is taller than or equal to the height at our left
            pointer, then we have two possible situations.
                We either are descending (if the left pointer is next to the right
                pointer).
                    If this is the case, we just need to reset our left pointer to
                    where our current right pointer is.
                Or we found the next bookend height.
                    If this is the case, we need to add the valley's area to our sum
                    and then reset our left pointer to where our current right pointer is.

            If we run into a height that is shorter than the height at our left pointer
                We just need to add the difference between it and the first bookend to
                our growing sum of valley area.

            The problem is that we don't know which of the two bookend will be the
            shorter of the two until we reach it, which makes calculating the valley
            area along the way difficult.

            We could potentially iterate until our right pointer finds a bookend.
            Then we could walk our left pointer forward to reach the right pointer,
            calculating the area in that valley along the way since we would then know
            the shorter of the two bookends.

        The problem with this line of thinking is that it doesn't take into account
        even higher maximums beyond the local maximums it finds.

        -----
        The key insight in this algorithm is that the smaller of the two maximums is the
        bottleneck. It doesn't matter if the left maximum is 10 if the right maximum is
        5. We can only hold as much water as the smaller of the two maximums.
        
        In this strategy we iterate through our input array three times.
        The first two times we note the left and right maximum for every index in our 
        input array.
        
        Then, once we know the left and right maximum for every index, we iterate a 
        third time to compute the amount of rain we could collect.

        This algorithm runs in O(n) time complexity with O(n) space complexity.
        They key insight here is that any given space can only hold water if the
        smaller of the two maximums on each side is greater than that space.
        """
        left, max_left = 0, []
        for height in heights:
            max_left.append(left)
            left = max(left, height)

        print(max_left)

        right, max_right = 0, [0] * len(heights)
        for i in reversed(range(len(heights))):
            max_right[i] = right
            right = max(right, heights[i])

        print(max_right)

        res = 0
        for i in range(len(heights)):
            rain = min(max_left[i], max_right[i]) - heights[i]
            res += rain if rain > 0 else 0

        return res

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
heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
expected = 6
actual = solution.trap(heights)
assert actual == expected, f"Test 8 failed. Expected: {expected}, but got: {actual}"

print("All tests passed!")
