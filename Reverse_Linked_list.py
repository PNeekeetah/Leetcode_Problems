# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 12:53:52 2021

@author: Nikita
"""

class ListNode:
    """
    Initial version
    def __init__(self, x):
        self.val = x
        self.next = None
    """    
    def __init__(self,val, next_node = None):
        self.val = val
        self.next = next_node
        
    def get_next(self):
        return self.next
    
    def __str__(self):
        """
        if self.next:
            return "|{}|->|{}|".format(self.val,self.next.val)  
        else:
            """
        return "|{}|".format(self.val)
        
    def goThrough(self):
        current_node = self
        while not (current_node.next is None):
            print("Node.val = {} ".format(current_node.val) + "Node.next.val = {}".format(current_node.next.val) )
            current_node = current_node.next
        print("\n")
        
class Solution: 
    def __init__(self):
        pass
       
    def reverseList2(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        """
        3 Pointer linear method non-recursive
        """
        previous = None
        current = head
        next_node = None
        while current is not None:
            next_node = current.get_next() # get next node
            current.next = previous  # switch first current reference backwards
            previous = current  # previous node becomes current
            current = next_node      # current_node becomes previous            
        return previous
            
        
            
    """
    More elegant solution
    """
    def reverseList1(self, head: ListNode) -> ListNode:
        new_head = None
        def traverse(node : ListNode):
            nonlocal new_head
            if node.next is not None:
                next_node = traverse(node.next)
                next_node.next = node
            else:
                new_head = node
            return node
        
        if head:
            traverse(head)
            head.next = None
        
        return new_head       

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

solution = Solution()
head = solution.reverseList2(head)
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