"""
https://neetcode.io/problems/reverse-a-linked-list
https://leetcode.com/problems/reverse-linked-list/description/

Reverse a Linked List
Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

Example 1:
Input: head = [0,1,2,3]
Output: [3,2,1,0]

Example 2:
Input: head = []
Output: []

Constraints:
0 <= The length of the list <= 1000.
-1000 <= Node.val <= 1000
"""
from typing import Optional
from linked_list_node import ListNode, create_linked_list_from_list, compare_linked_lists

class Solution:
    def reverse_linked_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None

        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp

        return prev

solution = Solution()

test_cases = [
    {"input": [0, 1, 2, 3], "expected": [3, 2, 1, 0], "description": "Example from problem statement"},
    {"input": [], "expected": [], "description": "Empty list"},
    {"input": [1], "expected": [1], "description": "Single element list"},
    {"input": [1, 2], "expected": [2, 1], "description": "Two element list"},
    {"input": [1, 2, 3, 4, 5], "expected": [5, 4, 3, 2, 1], "description": "Multiple elements list"}
]

for i, test in enumerate(test_cases, 1):
    input_list = create_linked_list_from_list(test["input"])
    expected_list = create_linked_list_from_list(test["expected"])
    actual_list = solution.reverse_linked_list(input_list)
    assert compare_linked_lists(expected_list, actual_list), (f"Test {i} ({test['description']}) failed. Expected:"
                                                              f" {expected_list}, "
                                                              f"but got: {actual_list}")

print("All tests passed!")