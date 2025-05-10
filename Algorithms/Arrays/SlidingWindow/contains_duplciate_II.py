"""
https://leetcode.com/problems/contains-duplicate-ii/description/?envType=problem-list-v2&envId=sliding-window

219. Contains Duplicate II
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such
that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false

Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
"""


class Solution:
    def containsNearbyDuplciate(self, nums: list[int], k: int) -> bool:
        """
        We are looking for two numbers that are equal to each other within our input list.
        We have the additional condition that the difference between these indices is smaller than k.

        This means our second index can be up to k larger than the first index.
        This means that numbers that we consider for duplicates must be within a window of size k.

        We could use a hash map to store the values that we have seen.
        We could use two pointers, l and r, to represent our sliding window.
        We could add and remove values from our hashmap as we move our window along.

        We iterate through our input list adding a count of the number we see to our hashmap, seen, along the way.
        If the window becomes bigger than k, then we move our left pointer, l, over and remove a count of nums[l] from
        seen.
        If we then look at our hashmap and find a count that is greater than zero for the value of nums at our right
        pointer, r, then we instantly return True because we've found numbers that satisfy the conditions.
        We then add a count of nums[r] to our hashmap.
        Finally, we return False if we finish the entire iteration and don't find numbers that satisfy our conditions.

        O(n) Space and Time complexity.

        We could maybe conditionally remove our key,value pairs from our hashmap and improve our space complexity to
        O(k).
        """

        seen = {}
        l = 0

        for r in range(len(nums)):
            num = nums[r]

            if r - l > k:
                seen[nums[l]] -= 1
                l += 1

            if seen.get(num, 0) >= 1:
                return True

            seen[num] = 1 + seen.get(num, 0)

        return False


solution = Solution()

test_cases = [
    {
        "nums": [1, 2, 3, 1],
        "k": 3,
        "expected": True,
        "description": "Duplicate 1 within distance 3"
    },
    {
        "nums": [1, 0, 1, 1],
        "k": 1,
        "expected": True,
        "description": "Duplicate 1 within distance 1"
    },
    {
        "nums": [1, 2, 3, 1, 2, 3],
        "k": 2,
        "expected": False,
        "description": "No duplicates within distance 2"
    },
    {
        "nums": [1, 2, 3, 4, 5],
        "k": 3,
        "expected": False,
        "description": "No duplicates in the array"
    },
    {
        "nums": [1, 1],
        "k": 0,
        "expected": False,
        "description": "Duplicate 1 but distance is 0"
    },
    {
        "nums": [1, 2, 3, 1],
        "k": 0,
        "expected": False,
        "description": "Duplicate 1 but distance is greater than 0"
    },
    {
        "nums": [1],
        "k": 1,
        "expected": False,
        "description": "Single element, no duplicates"
    },
    {
        "nums": [1, 2, 3, 1, 2, 3],
        "k": 5,
        "expected": True,
        "description": "Duplicate 1 within distance 5"
    }
]

for i, test in enumerate(test_cases, 1):
    result = solution.containsNearbyDuplciate(test["nums"], test["k"])
    assert result == test["expected"], (
        f"Test {i} ({test['description']}) failed. "
        f"Expected {test['expected']}, but got {result}"
    )

print("All tests passed!")
