"""

 Swap Nodes in Pairs
Medium


Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

 

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.


"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        
        if not head.next:
            return head
        
        temp = head.val
        head.val = head.next.val
        head.next.val = temp
        
        head.next.next = self.swapPairs(head.next.next)
        
        return head