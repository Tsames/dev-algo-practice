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
from typing import Optional


class LinkedListNodeRandom:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = x
        self.next = next
        self.random = random

def create_linked_list_random(nodes: list[list[int]]) -> Optional[LinkedListNodeRandom]:
    if not nodes:
        return None

    nodes_map = {None : None}
    dummy = LinkedListNodeRandom(None)
    prev = dummy

    for i in range(len(nodes)):
        newNode = LinkedListNodeRandom(nodes[i][0])
        nodes_map[i] = newNode
        prev.next = newNode
        prev = prev.next

    for j in range(len(nodes)):
        node = nodes_map[j]
        node.random = nodes_map[nodes[j][1]]

    return dummy.next

def compare_linked_lists_random(l1: Optional[LinkedListNodeRandom], l2: Optional[LinkedListNodeRandom]) -> bool:
    while l1 and l2:
        if l1.val != l2.val:
            return False
        l1 = l1.next
        l2 = l2.next
    return l1 is None and l2 is None

class Solution:
    def copy_random_list(self, head: Optional[LinkedListNodeRandom]) -> Optional[LinkedListNodeRandom]:
        """
        The challenging part of this algorithm is the random property.
        If the random property were not present, we would be able to create a deep copy by iterating through our
        input linked list, creating a copy at each node and setting the previous nodes' next value to the new node we
        just created.

        However, the random property complicates this because we may not have created that node yet.
        So, to overcome this issue we are going to iterate through our given linked list twice.
        The first time, we will create deep copies, and to be able to access them easily and quickly (without having
        to traverse our linked list each time) we will store them in hashmap with the original node as the key and
        the deep copy node as the value.

        Then, in the second iteration we will be able to set the random property with ease.
        """

        node_map = {None : None}
        # Since we are iterating through our linked list twice, we need a separate variable so we can reset our
        # iteration back to the beginning.
        curr = head

        # Pass number one, create the deep copy nodes
        while curr:
            node_map[curr] = LinkedListNodeRandom(curr.val)
            curr = curr.next

        # Pass Number two, setting random and next for our deep copy nodes using our hashmap
        curr = head
        while curr:
            deep_copy = node_map[curr]

            deep_copy.random = node_map[curr.random]
            deep_copy.next = node_map[curr.next]
            curr = curr.next

        return node_map[head]

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
    head = create_linked_list_random(test["input"])
    expected = create_linked_list_random(test["expected"])
    result = solution.copy_random_list(head)
    assert compare_linked_lists_random(result, expected), (
        f"Test {i} ({test['description']}) failed. "
        f"Expected: {test['expected']}, but got: {result}"
    )

print("All tests passed!")
