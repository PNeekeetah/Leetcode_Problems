# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 11:10:30 2021

@author: Nikita
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

class Solution:
     def nextLargerNodes(self, head: ListNode): #-> List[int]:   Friend's solution
        v=[]
        act=head
        while (not(act is None)):
            v.append(act.val)
            act=act.next
        stack=[v[-1]]
        rez=[0]
        i=len(v)-2
        while (i>=0):
            if (stack[-1]>v[i]):
                rez.append(stack[-1])
            else:
                while (len(stack)>0 and stack[-1]<=v[i]):
                    stack.pop()
                if (len(stack)==0):
                    rez.append(0)
                else:
                    rez.append(stack[-1])
            stack.append(v[i])
            i=i-1
        rez.reverse()
        return rez

l7 = ListNode(1)
l6 = ListNode(5,l7)
l5 = ListNode(2,l6)
l4 = ListNode(9,l5)
l3 = ListNode(1,l4)
l2 = ListNode(5,l3)
l1 = ListNode(7,l2)
l0 = ListNode(1,l1)


sol = Solution()
hello = sol.nextLargerNodes(l0)    

"""
I've thrown in the towel after 1 hour and 39 minutes.

I figured out what I need to do with regards to the algorithm pen and 
paper wise, but I don't seem to be able to implement it. God knows why.
I've put my friend's solution here, hoping that i'll come back to this
problem at one point and solve it myself.
"""