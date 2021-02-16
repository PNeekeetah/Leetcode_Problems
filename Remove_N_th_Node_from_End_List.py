# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 22:16:24 2021

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
        return None
    
    def removeNthFromEnd1(self, head: ListNode, n: int) -> ListNode: # my own
    
        nodes_list = list()
        current_node = head
        while not(current_node.next is None):
            nodes_list.append(current_node)
            current_node = current_node.next
        nodes_list.append(current_node)
        if (len(nodes_list) == 1):
            return None
        else:
            if (n != 1):
                nodes_list[-n].val = nodes_list[-n + 1].val
                nodes_list[-n].next = nodes_list[-n + 1].next
            else:
                nodes_list[-n-1].next = None 
        return head
        

    def deleteNthFromEnd2(self, head : ListNode, n : int) -> ListNode: # How I would have done it knowing the "head pointer" trick
        first = head
        second = head
        #
        for i in range (n):
            second = second.next
            
        if not(second):
            return head.next
            
        while not(second.next == None):
            first = first.next
            second = second.next
        
        if (n == 1):
            first.next = None
        else:    
            first.next.val = first.next.next.val
            first.next.next = first.next.next.next
            """
            I needn't do it like this; I could have done first.next = first.next.next
            Remember, change only the reference, not the entire thing.
            """
            
        return head


head   = ListNode(0)
node_1 = ListNode(1)
node_2 = ListNode(2)
node_3 = ListNode(3)
node_4 = ListNode(4)
head.next = node_1
node_1.next = node_2
node_2.next = node_3
node_3.next = node_4

sol = Solution()
head = sol.deleteNthFromEnd3(head,5)
head.goThrough()  
"""
The way I thought about it was keeping track of all the nodes that were visited
in the linked list, then deleting the last one. 

The smart solution was to "set sail" for one pointer, and once it is N ahead
of the first one, launch a second one.
"""