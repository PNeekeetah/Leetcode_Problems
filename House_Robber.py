# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 19:10:29 2021

@author: Nikita
"""
import numpy as np

from binarytree import tree, bst, heap
from binarytree import Node

l = [1,2,3,4,5,6,7,8,9]
l = [51,6,2,0,41,0,500]
#l = [3,24,5,2,0]
#l = np.array([1,2,3,4,5,78,29,1,2])
t1 = [2,5,64,41,132,4,1,2,4,5,1,2,4,6,2,7,72,2,1,243,5,1,2,3,1,1,1,1,1,2,3,4,5,6,7,3,6,7,38,8,3,32,1,1,24,62,2,2,2,2]


class Solution:
    def rob(self, nums: list()) -> int:
        seen = {}
        def robFrom(position, nums):
            nonlocal seen
            if position >= len(nums):
                return 0
            if seen.get(position) != None:
                return seen[position]
            
            answer = max(robFrom(position+1,nums), robFrom(position+2,nums) + nums[position])
            seen[position] = answer
            return answer
                
        return robFrom(0,nums)



"""
After a couple of weeks, I decided to come back to this problem and solve it.

I still didn't manage to get it quite right, so I've thrown in the towel for 
this problem. 

"""


"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class TreeTraversal:
    def __init__(self):
        self.all_sums = []
        self.vis = {}
        
    # Left, Node, Right
    def dfs_inorder(self, node: TreeNode,total : int):
        if not(self.vis.get(node)):
            self.vis[node] = 1
            if (node.left):
                self.all_sums.append(total + node.left.val)
                self.dfs_inorder(node.left, total + node.left.val )
    
            if(node.right):
                self.all_sums.append(total + node.right.val)
                self.dfs_inorder(node.right, total + node.right.val )
            
def build_tree(nums : list,s : int, decision : int, seen_states = None):
    
    if (decision >= len(nums)-1):
        return
    
    node = Node(s) 
    node.left = build_tree(nums,s + nums[decision],decision + 2)
    node.right = build_tree(nums,s + nums[decision + 1] , decision + 3)
    
        
    return node

root = build_tree(l,0,0) 
print (root)

traversal = TreeTraversal()
traversal.dfs_inorder(root,0)
var1 = 0
for m in traversal.all_sums:
    if m > var1:
        var1 = m
        


def rob_house(decision : int, nums : list, total : int, seen_states = None):
    if not(seen_states):
        seen_states = {}
    if (decision >= len(nums)-1):
        return
    if not(seen_states.get((decision,0))):
        seen_states[(decision,0)] = total + nums[decision]
        rob_house(decision + 2, nums, seen_states[(decision,0)],seen_states)
    else:
        if (total > seen_states[(decision,0)]):
            seen_states[(decision,0)] = total
            rob_house(decision + 2, nums, seen_states[(decision,0)],seen_states)
    
    if not(seen_states.get((decision,1))):
        seen_states[(decision,1)] = total + nums[decision+1]
        rob_house(decision + 3, nums, seen_states[(decision,1)],seen_states)
    else:
        if (total > seen_states[(decision,1)]):
            seen_states[(decision,1)] = total
            rob_house(decision + 3, nums, seen_states[(decision,1)],seen_states)
    return seen_states
        


import numpy as np
import random

hello = [ random.randint(1,100) for i in range(0,20)]

states = rob_house(0,t1,0)
maxim = 0
for val in states.values():    
    if val > maxim:
        maxim = val
total_sum = 0
i = 0
while(i < len(l)-2):
    if (l[i] + l[i+2] > l[i+1]):
        total_sum += l[i]
    else:
        total_sum += l[i+1]
    i += 2


I inadvertently stopped the timer at 39 minutes and 46 seconds.
I started a new one.

Anyway, I just had a flash. If the array is sorted, all we need to do
is get it's length and then if it's odd, pick every second element 
starting from 2, otherwise pick every first element. 

The solution should be O n log n like this (with merge sort)

Except that of course it's not that easy -> you lose the adjacency
of 2 houses doing this.

Okay, I could perhaps organize my problem like a tree as follows:
    at first point, decide if I take the first house or not.
        if I take it, I have to the the 2nd next
        if I don't take it, I can take the next one
        
Essentially, all points present me with this choice. let me 
map out a tree in paint really quickly. 

Alright, so, for list l = [3,24,5,2,0] I've drawn a tree. The tree
looks exponential, having a depth of 5. For 5 items, it has 12 nodes.

Now here's the question. If I make an algorithm that makes the optimal
choice at each step, does it guarantee that I will always make the 
optimal choice?

In this case, the optimal subcoice is always : do I pick the
first and the third, or do I take the second with the promise that
the fourth could be a lot better.

With these numbers 3 , 24, 5 it's easy to pick the second one. 
However, what if I have 3,5, 24,400. It's easy for me to pick first 
and third when faced with the first decision, but then I miss out
on 400.

Well, congrats me. I've just arrived at the conclusion that always
taking the optimal sub path doesn't result in the overall optimal
global path.  

I spent another 3 hours, 19 minutes and 21 seconds on this problem.
The only solution I had was to build a divide and conquer recursive
approach. It didn't work out yet, but i'll leave it here for 
tomorrow.

Okay, after another 24 minutes and 46 seconds I give up.


Another 45 minutes 37 went by

l = [1,2,3,4,5,6,7,8,9,10]

def pick (nums : list, decision : int, seen = None):
    
    if (seen == None):
        seen = {}
        
    if (decision >= len(nums) ):
        return 
    
    if not (seen.get((decision,0))):
        seen[(decision,0)] = 1
        decision(nums, decision + 2, seen)
    
    if not (seen.get((decision,1))):
        seen[(decision,1)] = 1
        decision(nums, decision + 3, seen)
        
    return seen

states = decision(l,0)

Today's attempt.

"""