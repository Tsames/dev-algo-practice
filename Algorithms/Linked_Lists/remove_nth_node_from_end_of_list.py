"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
https://neetcode.io/problems/remove-node-from-end-of-linked-list

Remove Nth Node From End of List
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""
from linked_list_node import ListNode, create_linked_list, compare_linked_lists

class Solution:
    def remove_nth_from_end(self, head: ListNode, n: int) -> ListNode:
        """
        The main issue in this problem is that we don't know the length of our input linked list upfront.
        That means that we don't know when we are at the last nth node.

        Now we could count the number of nodes by iterating through our list once.
        We could then know the number
        """
        linked_list_length = 0
        dummy = ListNode(None, head)
        cur = head

        while cur:
            linked_list_length += 1
            cur = cur.next

        cur = dummy
        while linked_list_length > n:
            cur = cur.next
            linked_list_length -= 1

        cur.next = cur.next.next if cur.next else None
        return dummy.next

solution = Solution()

test_cases = [
    {"input": [1, 2, 3, 4, 5], "n": 2, "expected": [1, 2, 3, 5], "description": "Remove 2nd node from end"},
    {"input": [1], "n": 1, "expected": None, "description": "Single node list, remove the only node"},
    {"input": [1, 2], "n": 1, "expected": [1], "description": "Two nodes, remove last node"},
    {"input": [1, 2], "n": 2, "expected": [2], "description": "Two nodes, remove first node"},
    {"input": [1, 2, 3, 4, 5], "n": 5, "expected": [2, 3, 4, 5], "description": "Remove head node"},
    {"input": [1, 2, 3, 4, 5], "n": 1, "expected": [1, 2, 3, 4], "description": "Remove last node"}
]

for i, test in enumerate(test_cases, 1):
    head = create_linked_list(test["input"])
    expected = create_linked_list(test["expected"])
    result = solution.remove_nth_from_end(head, test["n"])
    assert compare_linked_lists(result, expected), (
        f"Test {i} ({test['description']}) failed. "
        f"Expected: {test['expected']}, but got: {result}"
    )

print("All tests passed!")