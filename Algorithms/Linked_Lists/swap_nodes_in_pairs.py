from Algorithms.Linked_Lists.linked_list_node import ListNode

"""
Given a linked list, swap every two adjacent nodes and return its head.
You must solve the problem without modifying the values in the list's nodes
(i.e., only nodes themselves may be changed.)


Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:
Input: head = []
Output: []

Example 3:
Input: head = [1]
Output: [1]

Example 4:
Input: head = [1,2,3]
Output: [2,1,3]

Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
"""

# One thing to keep in mind is that if we are swapping nodeB and nodeC,
# we must keep nodeA in memory since we cannot go backwards in a normal linked list.
# We also have to keep references for the next node in the pair and the node that comes after that
# because we will be changing the order of the linked list


def switchNodesInPairs(node: ListNode) -> ListNode:
    res = ListNode(None, node)
    lastNodeVisited = res

    while node and node.next:
        # Save references to all necessary nodes
        pairNode = node.next
        nodeNextToPair = pairNode.next

        # Shuffle Nodes
        lastNodeVisited.next = pairNode
        pairNode.next = node
        node.next = nodeNextToPair

        # Set pointers for next iteration
        lastNodeVisited = node
        node = node.next

    return res.next


# Test One
testOneNodeHead = ListNode(1)
testOneNodePointer = testOneNodeHead
for i in range(2, 5):
    newNode = ListNode(i)
    testOneNodePointer.next = newNode
    testOneNodePointer = newNode

print(switchNodesInPairs(testOneNodeHead))

# Test Two
testTwoNodeHead = ListNode()
print(switchNodesInPairs(testTwoNodeHead))

# Test Three
testThreeNodeHead = ListNode(1)
print(switchNodesInPairs(testThreeNodeHead))
