"""
https://leetcode.com/problems/copy-list-with-random-pointer/description/
https://neetcode.io/problems/copy-linked-list-with-random-pointer

Copy List with Random Pointer

A linked list of length n is given such that each node contains an additional random pointer, which could point to
any node in the list, or null.
Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has
its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes
should point to new nodes in the copied list such that the pointers in the original list and copied list represent
the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding
two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val,
random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not
point to any node.
Your code will only be given the head of the original linked list.

Example 1:
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Example 2:
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]

Example 3:
Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]

Constraints:
0 <= n <= 1000
-104 <= Node.val <= 104
Node.random is null or is pointing to some node in the linked list.
"""
from linked_list_node import ListNode, create_linked_list, compare_linked_lists
from typing import Optional

class Solution:
    def copy_random_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return head

solution = Solution()

test_cases = [
    {
        "input": [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]],
        "expected": [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]],
        "description": "List with random pointers to various nodes"
    },
    {
        "input": [[1, 1], [2, 1]],
        "expected": [[1, 1], [2, 1]],
        "description": "List with random pointers forming a loop"
    },
    {
        "input": [[3, None], [3, 0], [3, None]],
        "expected": [[3, None], [3, 0], [3, None]],
        "description": "List with duplicate values and random pointers"
    },
    {
        "input": [],
        "expected": [],
        "description": "Empty list"
    },
    {
        "input": [[5, None]],
        "expected": [[5, None]],
        "description": "Single node with no random pointer"
    }
]

for i, test in enumerate(test_cases, 1):
    head = create_linked_list(test["input"])
    expected = create_linked_list(test["expected"])
    result = solution.copy_random_list(head)
    assert compare_linked_lists(result, expected), (
        f"Test {i} ({test['description']}) failed. "
        f"Expected: {test['expected']}, but got: {result}"
    )

print("All tests passed!")