"""
Implement Insertion Sort

Insertion sort is an O(n^2) sorting algorithm that works by sorting growing subarrays.
The subarrays starts with just the first element at index 0 and grows to the right
until it is the entire input array.
"""

class Solution:
    def insertion_sort(self, nums: list[int]) -> list[int]:
        # Loop through our array, beginning at index 1 because we consider the subarray
        # of just the first element to already be sorted.
        for i in range(1,len(nums)):
            # Record the value at this position
            key = nums[i]
            # The last index of the sorted portion of our array.
            j = i -1

            """
            While that value is less than the jth position in our sorted subarray
            move that value down our subarray by setting each value to its slightly 
            larger neighboring index. 
            
            Once the looping stops, we've found a value that is less than our element.
            So place our element at the index to the right of it.
            """
            while j >= 0 and key < nums[j]:
                nums[j+1] = nums[j]
                j -= 1
            nums[j+1] = key

        return nums

solution = Solution()

# Test case 1: Unsorted array
expected = [1, 2, 3, 4, 5]
actual = solution.insertion_sort([3, 1, 5, 4, 2])
assert actual == expected, f"Test one failed. Expected: {expected}, but got: {actual}"

# Test case 2: Already sorted array (in descending order)
expected = [1, 2, 3, 4, 5]
actual = solution.insertion_sort([5, 4, 3, 2, 1])
assert actual == expected, f"Test two failed. Expected: {expected}, but got: {actual}"

# Test case 3: Array sorted in ascending order
expected = [1, 2, 3, 4, 5]
actual = solution.insertion_sort([1, 2, 3, 4, 5])
assert actual == expected, f"Test three failed. Expected: {expected}, but got: {actual}"

# Test case 4: Array with duplicate elements
expected = [1, 3, 3, 4, 5]
actual = solution.insertion_sort([3, 5, 1, 4, 3])
assert actual == expected, f"Test four failed. Expected: {expected}, but got: {actual}"

# Test case 5: Empty array
expected = []
actual = solution.insertion_sort([])
assert actual == expected, f"Test five failed. Expected: {expected}, but got: {actual}"

print("All tests passed!")