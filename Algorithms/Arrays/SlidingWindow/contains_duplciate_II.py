"""
https://leetcode.com/problems/contains-duplicate-ii/description/?envType=problem-list-v2&envId=sliding-window

219. Contains Duplicate II
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

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
    def containsNearbyDuplciate(self, nums: list[int], k:int) -> bool:
        #todo
        return True

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