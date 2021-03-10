# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 19:27:20 2021

@author: Nikita
"""
calls = 0
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # All values on the left of root are smaller
        # All values on the right of root are greater
        # Both the left and right subtrees are BSTs
        
        def divide(node : TreeNode):
            global calls
            calls += 1
            if not node:
                return True
            
            c1 = c2 = True
            if node.left:
                c1 = divide(node.left) and conquerLeft(node.left,node.val)  
            
            if node.right: 
                c2 =  divide(node.right) and conquerRight(node.right,node.val)
                
            return c1 and c2
            
        def conquerLeft(node : TreeNode, value : int):
            global calls 
            calls += 1
            if not node:
                return True
            return conquerLeft(node.left,value) and conquerLeft(node.right,value) and node.val < value
        
        def conquerRight(node : TreeNode, value : int):
            global calls
            calls += 1
            if not node:
                return True
            return conquerRight(node.left,value) and conquerRight(node.right,value) and node.val > value
                
        return divide(root)             

t9 = TreeNode(12)
t8 = TreeNode(11)
t7 = TreeNode(10)
t6 = TreeNode(7)
t5 = TreeNode(5)    
t4 = TreeNode(2,t9,t8)    
t3 = TreeNode(9,t6,t7)
t2 = TreeNode(4,t4,t5)    
t1 = TreeNode(6,t2,t3)

sol = Solution()
val = sol.isValidBST(t1) 
    
"""
Solved this problem previously, but I didn't do it recursively the whole way.
I wanted to use only recursion for this problem, and I managed to find A solution
in 52 minutes and 47 seconds.

The submission is a disaster in terms of both runtime and memory because of the
following.

At each step, I check that all nodes on the left of the current node have a 
lower value. I also check that all nodes on the right of the current node have 
a lower value. I also check the left and right subtrees at each point.

My initial solution did an inorder traversal and stored the elements into an array.
The array has to be be sorted in ascending order if it's a BST.

I don't actually know how to propagate at each step that the value should be 
lower than the root on the left and greater than the root on the right.

I think the runtime is N^2/2 for this algorithm/ I checked for 13 nodes and the 
number of calls was 85 (169/2) . For 7 nodes it was 33 calls (almost 49//2)

"""
