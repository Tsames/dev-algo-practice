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
import heapq as hq
from collections import Counter, deque


class Solution:
    def least_interval(self, tasks: list[str], n: int) -> int:
        """
        Okay, we need n intervals before completing a task of the same type.
        This means that tasks of the same type slow us down the most.
        If we had an array of distinct CPU tasks we could process them in m intervals, where m is the length of our
        input array n.

        It seems like the dominant strategy to get the fewest number of intervals needs to be leading with the task
        whose count in tasks is the highest. We then need to fill the intervals that would otherwise be idle with
        other distinct tasks, preferably leading with other tasks whose count is the highest to minimize the number
        of idle intervals.

        So the algorithm would go something like this:
        At each iteration choose the task with the highest remaining count
        Any task that we choose here must be available (meaning it's been n intervals since the last time we processed
        the same task).

        To do this we need to know how long it's been since the previous time this task has been chosen (not sure how
        best to keep track of this).
        We also need to know the count (thinking hash map for this initially).

        Since we are returning the minimum time, we don't actually care about which task is which, so long as we
        don't process the same task before n intervals have passed.

        We can use a max heap to keep track of the count of each task.
        We could use a queue of tuples to keep track of the count and the time it is available again.
        """
        # Create a max heap containing the counts of all distinct tasks
        count = Counter(tasks)
        max_heap = [-c for c in count.values()]
        hq.heapify(max_heap)

        q = deque()
        time = 0

        while max_heap or q:
            time += 1
            # print(f"Iteration {time}")
            # print(f"\tMax Heap is {max_heap} and queue is {q}.")

            # First check if the element in queue can be put back in the max heap
            # Aka, there is an element in the queue, and the first element's first index is equal to the time
            if q and q[0][1] < time:
                ready = q.popleft()
                # print(f"\tPopping from queue! ({ready[0]}, {ready[1]})")
                hq.heappush(max_heap, ready[0])

            # If there are tasks in the max_heap, then take them out, increment the negative count, and put in the
            # queue.
            if max_heap:
                next_task = hq.heappop(max_heap) + 1
                # print(f"\tPulling from max heap! {next_task - 1}")
                if next_task < 0:
                    # print(f"\tAdding to queue! ({next_task}, {time + n})")
                    q.append((next_task, time + n))

        return time


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
        "expected": 10,
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
