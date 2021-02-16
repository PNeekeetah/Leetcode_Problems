# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 18:18:27 2021

@author: Nikita
"""

# Definition for single linked list.
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
                   
    def deleteCurrent(self,node):
        current_node = self
        while not (current_node is node):
            current_node = current_node.next
        current_node.val = current_node.next.val
        current_node.next = current_node.next.next

    
    def getNode(self, position : int):
        current_node = self
        for i in range (0, position):
            if (current_node.next is None):
                raise Exception(" Node {} requested ; only {} nodes available.".format(position,i))
            current_node = current_node.next
        return current_node


"""
Written in words :
    
Node head gets created, has dangling pointer          -> Is current node
New node gets created with value                      -> currently not attached anywhere
new node becomes attached to previously created node  -> node becomes attached
new node becomes current node                         -> tail becomes current node 
"""        

head   = ListNode(0)
node_1 = ListNode(1)
node_2 = ListNode(2)
node_3 = ListNode(3)
node_4 = ListNode(4)
head.next = node_1
node_1.next = node_2
node_2.next = node_3
node_3.next = node_4

node_to_delete = node_2

#head.goThrough()
#head.deleteCurrent(node_2)
#head.goThrough()
head.deleteNthfromEnd(1)
head.goThrough()

    
"""
I swear, what has gotten into me. I thought about it waaaay too much. The 
description of the problem said clearly that I was being given access to the
node to be deleted directly.

I thought about doing something clever such as iterating through all remaining
nodes and doing
current.val = current.next.val
current.next = current.next.next
in a domino like manner. However, only one value needs to be updated.

The code is as simple as:

def deleteNode(self, node) # self is the Solution class on Leetcode
    node.val = node.next.val
    node.next = node.next.next
    

"""


