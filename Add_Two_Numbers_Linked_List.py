# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 13:41:20 2021

@author: Nikita
"""

class ListNode(object):
     def __init__(self, val=0, next_one=None):
         self.val = val
         self.next = next_one

l1 = [9,9,9,9,9,9,9] 
l2 = [9,9,9,9]

if (l1 != []):
    l1_head = ListNode(l1.pop, None)  
else:
    l1_head = ListNode(None, None)
if (l2 != []):
    l2_head = ListNode(l1.pop, None)
else:
    l2_head = ListNode(None,None)
    
lastNode = l1_head
    
while (l1 != []):
    currentNode = ListNode(l1.pop,None)
    lastNode.next = currentNode
    lastNode = currentNode
    
    
    """
    class Solution(object):
    def addTwoNumbers(self, l1, l2):
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        last_temp = 0
        l1_current = l1.data
        l2_current = l2.data
        head = ListNode()
        head_set = False
        while ( not(l1_current.next == None and l2_current.next == None)):
            curr_temp = ListNode()
            temp.next = curr_temp
            if(head_set == False):
                if  (l1_current.next == None):
                    l2_current = l2_current.next
                    temp = ListNode(l2_current.data + last_temp)
                elif(l2_current.next == None):
                    l1_current = l1_current.next
                    temp = ListNode(l1_current.data + last_temp)
                else:
                    l1_current = l1_current.next
                    l2_current = l2_current.next
                    temp = ListNode(l1_current.data + l2_current.data + last_temp)
                head = temp
                head.next = None
                head_set = True
            else:
                if  (l1_current.next == None):
                    l2_current = l2_current.next
                    temp = ListNode(l2_current.data + last_temp)
                elif(l2_current.next == None):
                    l1_current = l1_current.next
                    temp = ListNode(l1_current.data + last_temp)
                else:
                    l1_current = l1_current.next
                    l2_current = l2_current.next
                    temp = ListNode(l1_current.data + l2_current.data + last_temp)
            last_temp = temp.data // 10
        if (last_temp):
            l3.append(1)
    """
    