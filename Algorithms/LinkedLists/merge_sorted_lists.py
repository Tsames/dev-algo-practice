"""
https://neetcode.io/problems/merge-two-sorted-linked-lists
https://leetcode.com/problems/merge-two-sorted-lists/description/

Merge Two Sorted Linked Lists

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted linked list and return the head of the new sorted linked list.
The new list should be made up of nodes from list1 and list2.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,5]
Output: [1,1,2,3,4,5]

Example 2:
Input: list1 = [], list2 = [1,2]
Output: [1,2]

Example 3:
Input: list1 = [], list2 = []
Output: []

Constraints:
0 <= The length of each list <= 100.
-100 <= Node.val <= 100
"""
from linked_list_node import ListNode, create_linked_list_from_list, compare_linked_lists
from typing import Optional

class Solution:
    def merge_two_sorted_lists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = curr = ListNode()

        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        if l1:
            curr.next = l1
        else:
            curr.next = l2

        return dummy.next

solution = Solution()

test_cases = [
    {"list1": [1, 2, 4], "list2": [1, 3, 5], "expected": [1, 1, 2, 3, 4, 5],
     "description": "Example from problem statement"},
    {"list1": [], "list2": [1, 2], "expected": [1, 2], "description": "One empty list"},
    {"list1": [], "list2": [], "expected": [], "description": "Both lists empty"},
    {"list1": [1], "list2": [2], "expected": [1, 2], "description": "Single element lists"},
    {"list1": [1, 3, 5], "list2": [2, 4, 6], "expected": [1, 2, 3, 4, 5, 6], "description": "Interleaved lists"}
]

for i, test in enumerate(test_cases, 1):
    list1 = create_linked_list_from_list(test["list1"])
    list2 = create_linked_list_from_list(test["list2"])
    expected_list = create_linked_list_from_list(test["expected"])
    actual_list = solution.merge_two_sorted_lists(list1, list2)
    assert compare_linked_lists(expected_list, actual_list), (f"Test {i} ({test['description']}) failed. Expected:"
                                                              f" {expected_list}, "
                                                              f"but got: {actual_list}")

print("All tests passed!")