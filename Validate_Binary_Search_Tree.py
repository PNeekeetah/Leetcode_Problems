# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 16:37:54 2021

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
        # add center
        self.nodes_list.append(node)
        # add right
        if(node.right):
            self.dfs_inorder(node.right)
        
    # Node, Left, Right
    def dfs_preorder(self, node: TreeNode):
        # add center
        self.nodes_list.append(node)
        # left first
        if (node.left):
            self.dfs_preorder(node.left)
        # add right
        if(node.right):
            self.dfs_preorder(node.right)
        
    # Right, Node, Left
    def dfs_postorder(self, node : TreeNode):
        # left first
        if (node.left):
            self.dfs_postorder(node.left)
        # add right
        if(node.right):
            self.dfs_postorder(node.right)
        # add center
        self.nodes_list.append(node)

        

class Solution:
    def __init__(self):
        return None
        
    """Let's not talk about this"""        
    def isValidBST(self, root: TreeNode) -> bool:
        def lowerBranch(node : TreeNode, value : int) -> bool:
            # If it contains successors, check each
            if(not node ):
                return True
            if (node.val >= value):
                return False
            
            if (node.left and node.right):
                if (not ((node.left.val < value) and (node.right.val < value))):
                    return False
                return lowerBranch(node.left, value) and lowerBranch(node.right, value)
            elif (node.left):
                if (not (node.left.val < value)):
                    return False
                return lowerBranch(node.left, value)
            elif (node.right):
                if (not (node.right.val < value)):
                    return False
                return lowerBranch(node.right, value)
            return True
        
        def greaterBranch(node : TreeNode, value : int) -> bool:            
            # If it contains successors, check each
            if (not node):
                return True
            if (node.val <= value):
                return False

            if (node.left and node.right):
                if (not ((node.left.val > value) and (node.right.val > value))):
                    return False
                return greaterBranch(node.left, value) and greaterBranch(node.right, value)
            elif (node.left):
                if (not (node.left.val > value)):
                    return False
                return greaterBranch(node.left, value)
            elif (node.right):
                if (not (node.right.val > value)):
                    return False
                return greaterBranch(node.right, value)
            return True
        
        queue = []
        queue.append(root)
        current_node = None
        
        while (len(queue) > 0):
            current_node = queue.pop(0)
            check = True
            if (current_node.left):
                check = check and lowerBranch(current_node.left, current_node.val)
                queue.append(current_node.left)    
                if (not check):
                    return False
                
            if (current_node.right):
                check = check and (greaterBranch(current_node.right, current_node.val))
                queue.append(current_node.right)
                if (not check):
                    return False
        return True
            
    def isValidBSTBetter(self, root: TreeNode) -> bool:
        traversal = TreeTraversal()
        traversal.dfs_inorder(root)
        for i in range (len(traversal.nodes_list)-1):
            if(traversal.nodes_list[i].val >= traversal.nodes_list[i+1].val ):
                return False
        return True
            
    def isValidBSTBetterIter(self, root: TreeNode) -> bool:
        stack = []
        visited = []
        current_node = root
        while (len(stack) > 0 or current_node != None):
            if (current_node != None):
                stack.append(current_node)
                current_node = current_node.left
            else:
                current_node = stack.pop()
                visited.append(current_node)
                if (len(visited) >= 2):
                    if (visited[-2].val >= visited[-1].val ):
                        return False
                current_node = current_node.right

        return True            
            
        

        
root = TreeNode(6, None, None)
node1 = TreeNode(5, None, None)
node2 = TreeNode(8, None, None)
node3 = TreeNode(7, None, None)
node4 = TreeNode(9, None, None)
root.left = node1
root.right = node2
node2.left = node3
node2.right = node4

solution = Solution()
print(solution.isValidBSTBetterIter(root))
traversal = TreeTraversal()
traversal.dfs_postorder(root)
for node in traversal.nodes_list:
    print (node.val)

"""
I thinks this problem can VERY LIKELY be solved with an approach that's
similar to the previous one.

I am not 100% sure what should happen if the tree has only the root
OR if the tree has no elements. Those seem like valid binary search trees, 
so I will go on a limb and say that the check returns true for those as well.

Oh, wow, messed up the requirements; it was THE ENTIRE SUBTREE, not just the
left and the right none. This will require some redesign.

To be fair, I actually don't know how to do this iteratively without 
turning the problem into a mess.

The way I believe it should be done recursively is as follows : 
    for each node in the tree, check that ABSOLUTELY ALL nodes to their 
    left are smaller; then, check that all nodes to their right are greater.
    
Let's assume a valid BST of depth 3. The first one is compared against 3 nodes
so 3 comparisons/ then another 3.
The second is compared against 1, so 1/ then another one. -> 8
10 comparisons overall. 

God I butchered this exercise :) it took me 1 hour and 24 to FINALLY
have a succesful submission. Runtime is O(n^maybe) and space complexity is
O(gimme), no wonder it's likely the worst solution OR among the very worst
solutions. 

I have to go at it again and hopefully find a better solution.

#######################EDIT#############################################

After pondering for a bit and revisiting the whole preorder, postorder and 
inorder traversal thing, I can say quite confidently that this new solution
is a lot better and a lot more elegant.

To check, whether the Binary tree is valid, do the following:
    1. Inorder traversal of the tree
    2. Check that each 2 consecutive respect the relation val1 < val2.
    
A lot cleaner than the previous mess.

In terms of runtime, it beats only 45% of submissions and 20% in terms of 
memory. Still nothing to talk about back home. If I find a way to do it
iteratively, it will probably beat a lot of submissions in terms of memory.

################ Edit 2 ##########################################

Alright, I did cheat a bit. Rather than wracking my brains hard over how
on earth I might implement the iterative inorder DFS, i just went ahead 
and read a wikipedia article about how I might implement it.

After copying the pseudocode in python, I was able to get an edge over 
89% of the submissions in terms of runtime and get a better result than
81% in terms of memory. 

def isValidBST(self, root: TreeNode) -> bool:
        stack = []
        current_node = root
        previous_node = None
        while (len(stack) > 0 or current_node):
            if (current_node):
                stack.append(current_node)
                current_node = current_node.left
            else:
                current_node = stack.pop()
                if (previous_node) and (previous_node.val >= current_node.val):
                    return False
                previous_node = current_node
                current_node = current_node.right

        return True            

This is the code I ended up using / i didn't use a "visited" vector.

The best submissions in term of runtime ended up being the recursive 
ones where they checked the values inside of the recursive calls 
(rather than appending the nodes to a list, then checking again).
"""