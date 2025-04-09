"""
https://neetcode.io/problems/linked-list-cycle-detection
https://leetcode.com/problems/linked-list-cycle/description/

Linked List Cycle Detection
Given the beginning of a linked list head, return true if there is a cycle in the linked list. Otherwise, return false.

There is a cycle in a linked list if at least one node in the list that can be visited again by following the next pointer.

Internally, index determines the index of the beginning of the cycle, if it exists. The tail node of the list will set it's next pointer to the index-th node. If index = -1, then the tail node points to null and no cycle exists.

Note: index is not given to you as a parameter.

Example 1:
Input: head = [1,2,3,4], index = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], index = -1
Output: false

Constraints:
1 <= Length of the list <= 1000.
-1000 <= Node.val <= 1000
index is -1 or a valid index in the linked list.
"""
from typing import Optional
from linked_list_node import ListNode, create_linked_list, create_cycle_list, compare_linked_lists

class Solution:
    def has_cycle(self, head: Optional[ListNode]) -> bool:
        """
        O(n) time and space complexity
        """
        visited = set()
        
        while head:
            if head in visited:
                return True
            visited.add(head)
            head = head.next
        
        return False
    
    def has_cycle_less_space(self, head: Optional[ListNode]) -> bool:
        """
        O(n) time and O(1) space complexity
        """        
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        return False

solution = Solution()

test_cases = [
    {"input": [1, 2, 3, 4], "index": 1, "expected": True, "description": "Cycle at index 1"},
    {"input": [1, 2], "index": -1, "expected": False, "description": "No cycle"},
    {"input": [1], "index": -1, "expected": False, "description": "Single element, no cycle"},
    {"input": [1, 2, 3, 4, 5], "index": 0, "expected": True, "description": "Cycle at index 0"},
    {"input": [1, 2, 3, 4, 5], "index": 4, "expected": True, "description": "Cycle at last element"}
]

for i, test in enumerate(test_cases, 1):
    input_list = create_cycle_list(test["input"], test["index"])
    expected = test["expected"]
    actual = solution.has_cycle(input_list)
    assert actual == expected, f"Test {i} ({test['description']}) failed for has_cycle. Expected: {expected}, but got: {actual}"
    actual = solution.has_cycle_less_space(input_list)
    assert actual == expected, f"Test {i} ({test['description']}) failed for has_cycle_less_space. Expected: {expected}, but got: {actual}"

print("All tests passed!")
