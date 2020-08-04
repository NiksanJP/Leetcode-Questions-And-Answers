"""

Add Two Numbers
Medium

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def getNum(n1):
            num = 0
            mul = 1
            
            while n1 != None:
                num += n1.val * mul
                mul *= 10
                n1 = n1.next
            return num
        
        val = getNum(l1) + getNum(l2)
        #807
        def getLinkedList(n):
            if len(n) == 1:
                return ListNode(int(n[-1]))
            
            b = ListNode(int(n[-1]))
            b.next = getLinkedList(n[:-1])
            
            return b
            
        
        return getLinkedList(str(val))
            