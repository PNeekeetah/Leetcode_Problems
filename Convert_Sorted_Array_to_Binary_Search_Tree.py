# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 12:02:38 2021

@author: Nikita
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class TreeTraversal:
    def __init__(self):
        self.nodes_list = []
        
    # Left, Node, Right
    def dfs_inorder(self, node: TreeNode):
        # left first
        if (node.left):
            self.dfs_inorder(node.left)
        # add center b
        self.nodes_list.append(node)
        # add right
        if(node.right):
            self.dfs_inorder(node.right)
            
    def dfs_inorder_iter(self, node : TreeNode):
        stack = []
        current_node = node
        while (len(stack) > 0 or current_node != None):
            if (current_node != None):
                stack.append(current_node)
                current_node = current_node.left
            else:
                current_node = stack.pop()
                self.nodes_list.append(current_node)
                current_node = current_node.right
        
        return self.nodes_list            
        
class Solution:
    def __init__(self):
        return None
    
    
    def sortedArrayToBST(self, nums: list) -> TreeNode:
        def divide(nums : list) -> TreeNode:
            length = len(nums)
            treeNode = TreeNode(nums[length//2])
            if length == 1:
                return 
            treeNode.left = divide(nums[0:length//2])
            treeNode.right = divide(nums[length//2:length])
        
            return treeNode
        if (len(nums) == 0):
            return None
        elif(len(nums) == 1):
            return TreeNode(nums[0])
        
        root = divide(nums)
        branch = root
        while(branch.left):
            branch = branch.left
        branch.left = TreeNode(nums[0])
        return root

l = [0,1,2,3,4,5,6,7,8,9]
solution = Solution()

bintree = solution.sortedArrayToBST(l)
branch = bintree

traversal = TreeTraversal()
traversal.dfs_inorder(bintree)
for node in traversal.nodes_list:
    print (node.val)
"""
The inorder traversal of a sorted binary tree produces a sorted array.
This must mean that a reverse process must produce the starting tree.

Alternatively, you could probably go with a divide and conquer approach 
where you continuously divide the array into sub arrays, then, when you reach
a single node, you start merging them together according to the following rules:
    
 if val1 < val2 -> new_node = TreeNode(val2), new_node.left = treenodeval1
 if val1 > val2 -> new_node = TreeNode(val2), new_node.right = treenodeval1
 # I actually don't know whether those rules are correct.
 
Submitted after 3 hours and 1 minute, first submission succesful.

Beats 99.48 % of submissions in terms of runtime and it apparently has
one of the highest memory consumptions. (this is no fluke, I tested it
3 times and I always got scores over 88%).

After scratching my head so much that I must have reached the brain, 
I came up with a solution that uses recursion. this wasn't intended
in the first place since my understanding of recursion is very bad,
but it somehow ended up like this.
I don't understand why it works, and frankly, after trying to come
up with a solution for 3 hours, I don't care. It works, it's good,
next problem.
 
One peculiarity is that whatever algorithm I might have come up with
manages to create only (n-1) nodes out of the n needed. It's always the
leftmost one. Since this is the case, I just added it at the end. 
It can probably be done in one go, but some other time.

All solutions seem to be doing the exact same thing; they build the 
tree recursively.
"""