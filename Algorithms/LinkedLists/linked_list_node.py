from typing import Optional


class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        res = ""
        node = self
        while node:
            res += f"({node.val}) -> "
            node = node.next

        return res


def create_linked_list_from_list(nodes: list[int]) -> ListNode:
    root = ListNode(nodes.pop(0))
    curr = root

    for node in nodes:
        newNode = ListNode(node)
        curr.next = newNode
        curr = newNode

    return root

def compare_linked_lists(l1: Optional[ListNode], l2: Optional[ListNode]) -> bool:
    while l1 and l2:
        if l1.val != l2.val:
            return False
        l1 = l1.next
        l2 = l2.next
    return l1 is None and l2 is None
