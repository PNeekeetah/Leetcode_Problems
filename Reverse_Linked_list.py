# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 12:53:52 2021

@author: Nikita
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
    def goThrough(self):
        current_node = self
        while not (current_node.next is None):
            print("Node.val = {} ".format(current_node.val) + "Node.next.val = {}".format(current_node.next.val) )
            current_node = current_node.next
        print("\n")
        
class Solution: 
    def __init__(self):
        next
        
    def reverseList(self, head: ListNode) -> ListNode:
        
        if not(head):
            return None
        
        elif not (head.next):
            return head
        
        first = head
        second =  head.next
        
        if not (second.next):
            second.next = first
            first.next = None
            return second

        aux_node = second.next
        second.next = first
        first.next = None
        first = second
        second = aux_node
            
        while (second.next):
            aux_node = second.next
            second.next = first
            first = second
            second = aux_node
                        
        second.next = first
        
        return second
    
    
head   = ListNode(0)
node_1 = ListNode(1)
node_2 = ListNode(2)
node_3 = ListNode(3)
node_4 = ListNode(4)
head.next = node_1
node_1.next = node_2
node_2.next = node_3
node_3.next = node_4
node_4.next = head

solution = Solution()
solution.reverseList(head)
head.goThrough()

"""
The possible edge cases could be:
    a) the node head is None -> first if takes care of this
    b) there is only 1 node -> second if statement takes care of this
    c) there are only 2 nodes -> third takes care of this
    Otherwise, execute while.
    
Finished this problem in 34 minutes and 49 seconds. 
No errors in the "reverseList" function because I spotted
them all before hitting "Run"
Beats 96.68% of all submissions in terms of runtime, 
accepted the first time it was submitted
Beats 78.79% of all submissions in terms of memory.

"""