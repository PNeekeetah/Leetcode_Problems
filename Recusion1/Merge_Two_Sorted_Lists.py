# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 17:27:59 2021

@author: Nikita
"""
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        def traverse(node1 : ListNode, node2 : ListNode):
            mergedList = None
            if not(node1):
                return node2
            if not(node2):
                return node1
            if (node1.val < node2.val):
                mergedList = node1
                mergedList.next = traverse(node1.next, node2)
            if (node2.val <= node1.val):
                mergedList = node2
                mergedList.next = traverse(node1, node2.next)
            return mergedList
        
        return traverse(l1,l2)

l8 = ListNode(5)
l7 = ListNode(4)
l6 = ListNode(7)
l5 = ListNode(6,l6)
l4 = ListNode(5,l5)
l3 = ListNode(4,l4)
l2 = ListNode(2,l3)
l1 = ListNode(1,l2)

solution = Solution()
h = solution.mergeTwoLists(l1,l8)

"""
I give up. After 3 hours and 24, I didn't manage to come up with a recursive
solution. 

Now, it's worth looking over what on earth that solution does.

So, you start out with both lists. You have 2 nodes, node1 and node2.
Node1 traverses the first lits, node2 traverses the second. 

If node1.val < node2.val, we don't know for certain that node1.next.val is greater
or lower than node2.val. For that reason, another node variable "merged"
takes the value of node1. The merge.next value depends on the call to traverse.


"""