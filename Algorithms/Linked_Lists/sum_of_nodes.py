from Algorithms.Linked_Lists.linked_list_node import ListNode

"""
Given a linked list and a sorted array of indices, return the sum of nodes at the indices.
For example, given a linked list:5 -> 6 -> 7 -> 8 -> 9
and indices array:[0, 2, 4]
You'll want to return the sum of the nodes at index 0, 2 and 4: 5 + 7 + 9 = 21

If any index is past the end of the linked list, just ignore it.

* [execution time limit] 4 seconds (py3)
* [memory limit] 1 GB
* [input] linkedlist.integer node
* [input] array.integer indices
* [output] integer
"""


def solution(node, indices):

    total = 0
    pointer = 0
    nodesVisited = 0

    while node and pointer < len(indices):
        if nodesVisited == indices[pointer]:
            total += node.value
            pointer += 1
        nodesVisited += 1
        node = node.next

    return total
