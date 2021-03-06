# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 21:16:05 2021

@author: Nikita
"""

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        def recSwap(head):
            if (head) and (head.next):
                head.val, head.next.val = head.next.val, head.val
                recSwap (head.next)
            return head
        return recSwap(head)
    
    def swapPairs1(self, head: ListNode) -> ListNode:
        def recSwap(node : ListNode):
            
            if  node and not (node.next):
                return node # return single node
            
            if node and node.next:
                curr_node = node
                next_node = node.next
                aux = recSwap(next_node.next)
                curr_node.next = aux
                next_node.next = curr_node
                return next_node
            
        return recSwap(head)
            
            
    

l8 = ListNode(8)
l7 = ListNode(7)
l6 = ListNode(6,l7)
l5 = ListNode(5,l6)
l4 = ListNode(4,l5)
l3 = ListNode(3,l4)
l2 = ListNode(2,l3)
l1 = ListNode(1,l2)

solution = Solution()
head = solution.swapPairs1(l1)
    
"""
Found a recursive solution in 24 minutes and 32 seconds.
Submission accepted from first try.

Beats 61.86 in terms of runtime and 52.88% in terms of memory.

The idea is to traverse every 2 nodes of the list. There are 2 possible cases
when we reach the end:
    1: There is one single node, in which case we return that 
    2: There are 2 nodes, in which case we swap the first with the second and
    we return the second
When exiting the recursive calls, we want to make sure that we reverse every 2 
nodes.

It took me an extra hour and 30 minutes to come up with a recursive solution 
that doesn't swap values. I've named the other solution swapPairs1.

I didn't try the iterative solution yet.

I believe I should try to keep track of the subproblems more often.



"""                    