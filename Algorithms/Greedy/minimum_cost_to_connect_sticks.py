"""
https://leetcode.com/problems/minimum-cost-to-connect-sticks/description/

1167. Minimum Cost to Connect Sticks
You have some number of sticks with positive integer lengths. These lengths are given as an array sticks,
where sticks[i] is the length of the ith stick.
You can connect any two sticks of lengths x and y into one stick by paying a cost of x + y. You must connect all the
sticks until there is only one stick remaining.
Return the minimum cost of connecting all the given sticks into one stick in this way.

Example 1:
Input: sticks = [2,4,3]
Output: 14
Explanation: You start with sticks = [2,4,3].
1. Combine sticks 2 and 3 for a cost of 2 + 3 = 5. Now you have sticks = [5,4].
2. Combine sticks 5 and 4 for a cost of 5 + 4 = 9. Now you have sticks = [9].
There is only one stick left, so you are done. The total cost is 5 + 9 = 14.

Example 2:
Input: sticks = [1,8,3,5]
Output: 30
Explanation: You start with sticks = [1,8,3,5].
1. Combine sticks 1 and 3 for a cost of 1 + 3 = 4. Now you have sticks = [4,8,5].
2. Combine sticks 4 and 5 for a cost of 4 + 5 = 9. Now you have sticks = [9,8].
3. Combine sticks 9 and 8 for a cost of 9 + 8 = 17. Now you have sticks = [17].
There is only one stick left, so you are done. The total cost is 4 + 9 + 17 = 30.

Example 3:
Input: sticks = [5]
Output: 0
Explanation: There is only one stick, so you don't need to do anything. The total cost is 0.

Constraints:
1 <= sticks.length <= 104
1 <= sticks[i] <= 104
"""
from heapq import heapify, heappop, heappush


class Solution:
    def connect_sticks(self, sticks: list[int]) -> int:
        """
        The examples are leading me to believe that the method that you ensure the minimum cost to connect sticks is
        by connecting the smallest stick together to create the smallest cost at each decision point.

        That makes some intuitive sense as you want to come up with the smallest total cost.
        The way to get the smallest total cost is to combine the smallest individual costs together.

        So if we believe that, then our problem becomes find the two smallest sticks (combined or not) and combine
        them together.

        It doesn't seem like we can do this easily without extra space.
        Without extra space, we would have to iterate through or list to find the next smallest stick each time.
        We would also have to have some method of removing sticks we've already combined and inserting new combined
        sticks.

        Since we are always looking for the minimum stick, it makes me think that a min heap would be useful here.
        We could create a min heap from our input list.
        We could pop from the heap to combine the smallest sticks each time.
        Then we could add back the combined stick to the heap.
        Once the min heap is of length 1, we could return the cost which we would keep track of with an outside
        variable.

        Cost to initially heapify: O(n)
        Cost to pop from the heap: O(log n)
        Cost to add to the heap: O(log n)

        O(n + n * 2log(n)) -> O(n * log(n))
        """
        heapify(sticks)
        cost = 0

        while len(sticks) > 1:
            smallest_combined_stick = heappop(sticks) + heappop(sticks)
            cost += smallest_combined_stick
            heappush(sticks, smallest_combined_stick)

        return cost


solution = Solution()

test_cases = [
    {
        "sticks": [2, 4, 3],
        "expected": 14,
        "description": "Basic test with three sticks"
    },
    {
        "sticks": [1, 8, 3, 5],
        "expected": 30,
        "description": "Test with four sticks"
    },
    {
        "sticks": [5],
        "expected": 0,
        "description": "Single stick, no cost required"
    },
    {
        "sticks": [1, 2, 3, 4, 5],
        "expected": 33,
        "description": "Test with multiple sticks in ascending order"
    },
    {
        "sticks": [10, 20, 30],
        "expected": 90,
        "description": "Test with larger stick lengths"
    },
    {
        "sticks": [1, 1, 1, 1],
        "expected": 8,
        "description": "Test with all sticks of equal length"
    }
]

for i, test in enumerate(test_cases, 1):
    result = solution.connect_sticks(test["sticks"])
    assert result == test["expected"], (
        f"Test {i} ({test['description']}) failed. "
        f"Expected {test['expected']}, but got {result}"
    )

print("All tests passed!")
