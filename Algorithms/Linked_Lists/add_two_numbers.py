"""
https://neetcode.io/problems/add-two-numbers

Add Two Numbers
You are given two non-empty linked lists, l1 and l2, where each represents a non-negative integer.
The digits are stored in reverse order, e.g. the number 123 is represented as 3 -> 2 -> 1 -> in the linked list.
Each of the nodes contains a single digit. You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Return the sum of the two numbers as a linked list.

Example 1:
Input: l1 = [1,2,3], l2 = [4,5,7]
Output: [5, 7, 0, 1]
Explanation: 321 + 654 = 975.

Example 2:
Input: l1 = [9], l2 = [9]
Output: [8,1]

Constraints:
1 <= l1.length, l2.length <= 100.
0 <= Node.val <= 9
"""
from typing import Optional
from Algorithms.Linked_Lists.linked_list_node import ListNode, create_linked_list

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        This problem is as much about addition as it is about linked list.
        Luckily, the lists are in reverse order, this makes carrying ones much, much, easier.
        
        First, we will want to make a dummy node for our output list.
        We also want a carry variable that keeps track of whether the previous iteration summed to a value greater than or equal to 10.
        
        We iterate as long as there are still elements in the first linked list (same as iterating through the second linked list since they are of equal size) or the carry value is non-zero.
        
        Each time, we will add the two numbers together plus the carry value.
        
        If that number is greater or equal to ten we will set the carry value to one again, otherwise set it to 0.
        
        Then we will construct a new ListNode with the remainder of our sum when divided by 10.
        """
        
        carry = 0
        dummy = curr = ListNode()
        
        while l1 or carry > 0:
            total = carry
            
            if l1:
                total += l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
                
            carry = total // 10
            
            newNode = ListNode(total % 10)
            curr.next = newNode
            curr = curr.next
        
        return dummy.next
                
solution = Solution()
print(solution.addTwoNumbers(create_linked_list([1, 2, 3]), create_linked_list([4, 5, 6])))
print(solution.addTwoNumbers(create_linked_list([9]), create_linked_list([9])))