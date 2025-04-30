"""
https://leetcode.com/problems/task-scheduler/description/

621. Task Scheduler
You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. Each CPU interval can be
idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to
be a gap of at least n intervals between two tasks with the same label.
Return the minimum number of CPU intervals required to complete all tasks.

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.
After completing task A, you must wait two intervals before doing A again. The same applies to task B. In the 3rd
interval, neither A nor B can be done, so you idle. By the 4th interval, you can do A again as 2 intervals have passed.

Example 2:
Input: tasks = ["A","C","A","B","D","B"], n = 1
Output: 6
Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.
With a cooling interval of 1, you can repeat a task after just one other task.

Example 3:
Input: tasks = ["A","A","A", "B","B","B"], n = 3
Output: 10
Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.
There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice
between repetitions of these tasks.

Constraints:
1 <= tasks.length <= 104
tasks[i] is an uppercase English letter.
0 <= n <= 100
"""


class Solution:
    def least_interval(self, tasks: list[str], n: int) -> int:
        # Todo
        return 0


solution = Solution()

test_cases = [
    {
        "tasks": ["A", "A", "A", "B", "B", "B"],
        "n": 2,
        "expected": 8,
        "description": "Basic test with a cooling interval of 2"
    },
    {
        "tasks": ["A", "C", "A", "B", "D", "B"],
        "n": 1,
        "expected": 6,
        "description": "Tasks with a cooling interval of 1"
    },
    {
        "tasks": ["A", "A", "A", "B", "B", "B"],
        "n": 3,
        "expected": 10,
        "description": "Tasks with a cooling interval of 3"
    },
    {
        "tasks": ["A", "A", "A", "A", "B", "B", "C", "C"],
        "n": 2,
        "expected": 10,
        "description": "Tasks with uneven frequencies and a cooling interval of 2"
    },
    {
        "tasks": ["A"],
        "n": 0,
        "expected": 1,
        "description": "Single task with no cooling interval"
    },
    {
        "tasks": ["A", "B", "C", "D", "E", "F"],
        "n": 2,
        "expected": 6,
        "description": "All tasks are unique with a cooling interval of 2"
    },
    {
        "tasks": ["A", "A", "A", "B", "B", "B", "C", "C", "D", "D"],
        "n": 2,
        "expected": 12,
        "description": "Tasks with multiple frequencies and a cooling interval of 2"
    }
]

for i, test in enumerate(test_cases, 1):
    result = solution.least_interval(test["tasks"], test["n"])
    assert result == test["expected"], (
        f"Test {i} ({test['description']}) failed. "
        f"Expected {test['expected']}, but got {result}"
    )

print("All tests passed!")
