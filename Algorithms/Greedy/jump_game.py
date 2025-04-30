"""
https://leetcode.com/problems/jump-game/description/

55. Jump Game
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the
array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.

Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it
impossible to reach the last index.

Constraints:
1 <= nums.length <= 104
0 <= nums[i] <= 105
"""


class Solution:
    def can_jump(self, nums: list[int]) -> bool:
        """
        This algo has a bit of an odd description.
        Each index of our input list represents the distance we can travel within our input list.
        We only have to determine if we can get to the final index.
        We do not have to determine which path has the fewest jumps, or list all possible paths.

        We know that our input list will be at least one element long.
        We also know that any given input can be at fewest 0, meaning we are never traveling backwards.

        ____
        Thought Process:
        ____

        We know ahead of time that this can be solved with a greedy algorithm.
        I don't think we could do something as simple as look at the possible next landing locations and choose the
        location with the biggest number. For this to not make the best pick, we would need a situation where an
        index with a less value got to a solution and the greater value did not. Maybe something like this:

        [4,2,0,0,1,1]

        Yeah, in this solution our simple selection of the greatest value does not get us to a solution,
        but a solution exists. So this does not work.

        I don't think we can simply choose the index that gets us the most distance each time either. Consider this
        example for such an approach.

        [4,4,0,0,0,1]

        We know that greedy algorithms typically make the best local decision at each index without needing to go back.
        This seems difficult since I can't think of a way to make that decision without knowing how it plays out
        later on.

        A key insight that we haven't remarked on yet is that since there are no negatives, we are really just trying
        to avoid 0s. Otherwise, we are happy to land on any other number. Additionally, each value represents the
        maximum distance we can go but does not necessitate that we travel the max distance. We can travel less
        distance too.

        Could we keep track of the distance we could potentially go, as we go?
        Maybe we could use a variable to keep track of the total distance we could potentially go.
        Maybe we call this variable jump.
        Jump might represent the furthest index that we can currently get to.
        Jump would start as the value of the zeroth index of nums, since that is where we start.

        jump = nums[0]
        Lets looks at the following example [4,0,0,2,0,1]

        If we ever find that jump >= len(nums) - 1 we can return true.
        If we get to the end of our loop and jump < len(nums) - 1, then we know we could never get to the final index.

        Let's walk through the example.
        We start with jump = 4 - which means the furthest that we can get is index 4.
        At index 1, we have a 0, which doesn't help us get any further, so move on.
        At index 2, we have another 0, move on.
        At index 3, we have a 2, which helps us get to index 5, 5 > 4 so replace jump.
        At index 4, another 0, move on.

        We probably have to add the condition that we can only replace jump with a value that we could get to.
        """
        jump = 0

        for i in range(len(nums)):
            if i <= jump:
                jump = max(jump, nums[i] + i)

        return jump >= len(nums) - 1

    def alternative_can_jump(self, nums: list[int]) -> bool:
        """
        Alternative solution where we move the goal back from the last position in our input list to an earlier
        position that still allows us to get to the end.

        If our goal is the starting position by the end, we know there is some solution.
        """
        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return goal == 0


solution = Solution()

test_cases = [
    {
        "nums": [2, 3, 1, 1, 4],
        "expected": True,
        "description": "Basic test where the last index is reachable"
    },
    {
        "nums": [3, 2, 1, 0, 4],
        "expected": False,
        "description": "Test where the last index is not reachable"
    },
    {
        "nums": [0],
        "expected": True,
        "description": "Single element array, already at the last index"
    },
    {
        "nums": [2, 0, 0],
        "expected": True,
        "description": "Test where jumps exactly reach the last index"
    },
    {
        "nums": [1, 1, 0, 1],
        "expected": False,
        "description": "Test where a zero blocks progress to the last index"
    },
    {
        "nums": [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
        "expected": True,
        "description": "Large jump at the start allows reaching the last index"
    }
]

for i, test in enumerate(test_cases, 1):
    result = solution.can_jump(test["nums"])
    assert result == test["expected"], (
        f"Test {i} ({test['description']}) failed. "
        f"Expected {test['expected']}, but got {result}"
    )

for i, test in enumerate(test_cases, 1):
    result = solution.alternative_can_jump(test["nums"])
    assert result == test["expected"], (
        f"Test {i} ({test['description']}) failed. "
        f"Expected {test['expected']}, but got {result}"
    )

print("All tests passed!")
