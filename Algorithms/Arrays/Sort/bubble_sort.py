"""
Implement Bubble Sort

Bubble sort is an O(n^2) sorting algorithm that sorts an array by swapping adjacent
elements.
"""

class Solution:
    def bubble_sort(self, nums: list[int]) -> list[int]:

        for i in range(len(nums)):
            swapped = False

            for j in range(len(nums) - 1):
                if nums[j] < nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    swapped = True
            if not swapped:
                break

        return nums

solution = Solution()

# Test case 1: Unsorted array
expected = [5, 4, 3, 2, 1]
actual = solution.bubble_sort([3, 1, 5, 4, 2])
assert actual == expected, f"Test one failed. Expected: {expected}, but got: {actual}"

# Test case 2: Already sorted array (in descending order)
expected = [5, 4, 3, 2, 1]
actual = solution.bubble_sort([5, 4, 3, 2, 1])
assert actual == expected, f"Test two failed. Expected: {expected}, but got: {actual}"

# Test case 3: Array sorted in ascending order
expected = [5, 4, 3, 2, 1]
actual = solution.bubble_sort([1, 2, 3, 4, 5])
assert actual == expected, f"Test three failed. Expected: {expected}, but got: {actual}"

# Test case 4: Array with duplicate elements
expected = [5, 4, 3, 3, 1]
actual = solution.bubble_sort([3, 5, 1, 4, 3])
assert actual == expected, f"Test four failed. Expected: {expected}, but got: {actual}"

# Test case 5: Empty array
expected = []
actual = solution.bubble_sort([])
assert actual == expected, f"Test five failed. Expected: {expected}, but got: {actual}"

print("All tests passed!")
