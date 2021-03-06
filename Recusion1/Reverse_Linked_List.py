# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 00:44:23 2021

@author: Nikita
"""
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
         
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        final_node = None
        def recursiveReverse(node):
            nonlocal final_node
            
            if (node) and not(node.next):
                final_node = node
                return node
            
            if (node) and (node.next):
                next_node = recursiveReverse(node.next)
                next_node.next = node
                return node
        recursiveReverse(head)
        head.next = None
        return final_node
    
l8 = ListNode(8)
l7 = ListNode(7)
l6 = ListNode(6,l7)
l5 = ListNode(5,l6)
l4 = ListNode(4,l5)
l3 = ListNode(3,l4)
l2 = ListNode(2,l3)
l1 = ListNode(1,l2)

solution = Solution()
head = solution.reverseList(l1)

"""
I got the recursive solution up and running in 19 minutes and 54 seconds. First
time submission.
It beats 88 % of the solutions in terms of runtime, but it has a high memory
usage.


"""