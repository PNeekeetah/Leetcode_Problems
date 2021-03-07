# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 01:54:33 2021

@author: Nikita
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> list():
        trees = []
        new_trees = []
        def gen(n):
            nonlocal trees, new_trees
            def treeDeepCopy (node : TreeNode) -> TreeNode:
                new_node = None
                if (node):
                    new_node = TreeNode(node.val)
                    new_node.left = treeDeepCopy(node.left)
                    new_node.right = treeDeepCopy(node.right)
                return new_node
            
            def insertTreeNode(root : TreeNode, node : TreeNode, asRoot : bool = True) -> list:
                nonlocal currentRoot,new_trees
                if (root):
                    if asRoot and node.val > root.val:
                        node.left = root
                        new_trees.append(treeDeepCopy(node))
                        node.left = None
                        insertTreeNode(root, node, False)
                    if not asRoot and node.val > root.val:
                        aux = root.right
                        root.right = node
                        node.left = aux
                        new_trees.append(treeDeepCopy(currentRoot))
                        root.right = aux            
                        insertTreeNode(root.right, node, False)
            if (n == 1):
                trees.append(TreeNode(1))
                return
                
            gen(n-1)
            node = TreeNode(n)
            for tree in trees:
                currentRoot = tree
                insertTreeNode(tree,node)
            trees = list(new_trees)
            new_trees.clear()
            
        
        gen(n)
        return trees
                
    
"""    
t3 = TreeNode(3)
t2 = TreeNode(2,None,t3)    
t1 = TreeNode(1,None,t2)

t4 = TreeNode(4)
"""

solution = Solution()
trees = solution.generateTrees(11)


    

"""
First submission succesful after 1 hour , 47 minutes and 7 seconds. 

This problem was NOT that difficult, but it was definitely prime choking
material. If i would have gotten this in an interview, I know I wouldn't have
gotten the job. 
I can't believe I got this right yet I didn't manage the Linked List one.

My solution beats 20% in terms of runtime. Here's the gist behind my solution:
    
    1.Each BST with nodes from 1 to n is built based on all BSTs with nodes from
    1 to n-1. As such, recursively go down to a BST with 1 node.
    
    2.From that point, start generating the new trees by inserting a node in the 
    old trees from call (n-1). The new trees are always built by inserting the
    new tree node to the right. Since the tree node's value is always larger than
    all the nodes in the tree, whenever it is inserted, it is inserted as the 
    right node. The subtree at that point is still a valid BST, so it is inserted
    to the left of the new node.
    

How many ways to build a BST with 1 node?

only 1 !

How many ways to build a BST with a node labelled 1 and a node
labelled 2?

2 -> one where 1 is root and 2 is to the right [1,null,2] OR
     one where 2 is root and 1 is to the left [2,1,null]
     
How many ways to build a BST with nodes labelled 1, 2 and 3?

I reckon we can build upon the previous example:
    
    in [1,null,2], we could insert 3 to the right of 1
    and 2 is appended as 3's left child
    we could insert 3 as 2's right child 
    
    we could insert 3 as 2's right child in case of [2,1,null]
    
    we can make 3 root in of [2,1, null] or root of [1,null,2]
    
    Overall, if we wanted a tree with 3 in it, there are 3 positions
    where we could insert it in the first tree and 3 positions where
    we could insert it in the second tree. There are 2 other trees
    with 3 as root. Out of the 3 ways to insert 3 in the first binary tree [1,null,2]
    
Anyhow, I need a way to insert a node in a BST and ensure that the BST remains
a BST.

     

"""