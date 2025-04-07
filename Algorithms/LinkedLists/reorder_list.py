"""
https://neetcode.io/problems/reorder-linked-list

Reorder Linked List
You are given the head of a singly linked-list.

The positions of a linked list of length = 7 for example, can intially be represented as:
[0, 1, 2, 3, 4, 5, 6]

Reorder the nodes of the linked list to be in the following order:
[0, 6, 1, 5, 2, 4, 3]

Notice that in the general case for a list of length = n the nodes are reordered to be in the following order:
[0, n-1, 1, n-2, 2, n-3, ...]

You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.

Example 1:
Input: head = [2,4,6,8]
Output: [2,8,4,6]

Example 2:
Input: head = [2,4,6,8,10]
Output: [2,10,4,8,6]

Constraints:
1 <= Length of the list <= 1000.
1 <= Node.val <= 1000
"""



'''
The difficulty with this problem is that you cannot traverse backwards in a linked list.

Instead, lets get two sub linked list.
Half of the first one and then the other half reversed.
Then it would be easy to interleave them in the desired manner.

To split the original list we use a fast and slow pointer.
Set the slow pointer to the original root node
Set the fast pointer to the next node

Reverse the second linked list
'''

def reorderLinkedList(root: ListNode) -> ListNode:
    if not root or root.next == None:
        return root
    
    slow = root
    fast = root.next
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    

















from Algorithms.LinkedLists.linked_list_node import ListNode, create_linked_list


def reorder_with_linear_space(root: ListNode) -> ListNode:
    nodes = []
    curr = root

    while curr:
        nodes.append(curr)
        curr = curr.next

    left_pointer = 0
    right_pointer = len(nodes) - 1

    while left_pointer < right_pointer:
        nodes[left_pointer].next = nodes[right_pointer]
        left_pointer += 1
        nodes[right_pointer].next = nodes[left_pointer]
        right_pointer -= 1

    nodes[right_pointer].next = None

    return root


# example_list = create_linked_list_from_list([1,2,3,4,5,6,7,8,9])
# print(example_list)
# reorder_with_linear_space(example_list)
# print(example_list)


def reorder_list(root: ListNode) -> ListNode:

    # Find the middle of the linked list
    slow_pointer = root
    fast_pointer = root.next

    while fast_pointer and fast_pointer.next:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next

    # Reorder the second half of the linked list
    reverse_list = slow_pointer.next
    slow_pointer.next = None

    previous_node = None

    while reverse_list:
        temp = reverse_list.next
        reverse_list.next = previous_node
        previous_node = reverse_list
        if not temp:
            break
        reverse_list = temp

    # Combine two seperate lists into one, and return it
    curr_list_one = root
    curr_list_two = reverse_list

    while curr_list_one or curr_list_two:
        temp = curr_list_one.next
        curr_list_one.next = curr_list_two
        curr_list_one = temp

        temp = curr_list_two.next
        curr_list_two.next = curr_list_one
        curr_list_two = temp

    return root


example_list_two = create_linked_list([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
print(reorder_list(example_list_two))
