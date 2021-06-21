# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 01:27:14 2021

@author: Nikita
"""

"""
Beats 32% in terms of memory
No data in terms of runtime.
"""

class Node:
    def __init__ (self, val : int, next_node : "Node" = None):
        self.val = val
        self.next = next_node
    
    def get_next (self):
        if self.next is not None:
            return self.next
        return None
    
    def get_val (self):
        return self.val
    
    def set_next (self, next_node : "Node"):
        self.next = next_node
        
    def set_val (self, val : int):
        self.val = val
    
class MyLinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.linked_list_length = 0
        
    def _initialize(self, val : int) -> None:
        self.head = Node(val)

    def get(self, index: int) -> int:
        print("Started get")
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index >= self.linked_list_length:
            return -1
        current = self.head
        while index > 0:
            current = current.get_next()
            index -= 1
        return current.get_val()
        

    def addAtHead(self, val: int) -> None:
        print("Started addAtHead")
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_node = Node(val, self.head)
        self.head = new_node
        self.linked_list_length += 1
        

    def addAtTail(self, val: int) -> None:
        print("Started addAtTail")
        """
        Append a node of value val to the last element of the linked list.
        """
        if self.linked_list_length == 0:
            self._initialize(val)
        new_node = Node(val)
        current = self.head
        while current is not None and current.get_next() is not None:
            current = current.get_next()
        
        if current is not None:
            current.set_next(new_node)
            self.linked_list_length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        print("Started addAtIndex")
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index == 0:
            self.addAtHead(val)
        elif index == self.linked_list_length:
            self.addAtTail(val)
        elif index > self.linked_list_length:
            return
        elif index > 0 and index < self.linked_list_length:
            current = self.head
            previous = None
            while index > 0:
                if index == 1:
                    previous = current
                current = current.get_next()
                index -= 1
            node = Node(val,current)
            previous.set_next(node)
            self.linked_list_length += 1

    def deleteAtIndex(self, index: int) -> None:
        print("Started deleteAtIndex")
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index >= self.linked_list_length:
            return 
        elif index == 0:
            self.head = self.head.get_next()
            self.linked_list_length -= 1
        else:
            previous = None
            current = self.head
            while index > 0:
                if index == 1:
                    previous = current
                current = current.get_next()
                index -= 1

            previous.set_next(current.get_next())
            self.linked_list_length -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)