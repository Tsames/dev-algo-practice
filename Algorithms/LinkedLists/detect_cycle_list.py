"""
https://neetcode.io/problems/linked-list-cycle-detection

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
from Algorithms.LinkedLists.linked_list_node import ListNode, create_linked_list_from_list

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
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
    
    def hasCycleBetter(self, head: Optional[ListNode]) -> bool:
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
cycleList = create_linked_list_from_list([1, 2, 3, 4, 5])
nonCycleList = create_linked_list_from_list([1, 2, 3, 4, 5])

tail = cycleList
while tail.next:
    tail = tail.next

tail.next = cycleList

print(solution.hasCycle(cycleList) == True)
print(solution.hasCycle(nonCycleList) == False)

print(solution.hasCycleBetter(cycleList) == True)
print(solution.hasCycleBetter(nonCycleList) == False)
