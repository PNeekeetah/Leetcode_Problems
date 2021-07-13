"""
First time submission succesful.
It beats 62% in terms of runtime and 0% 
in terms of memory.

Admittedly, I was supposed to do this using
an iterative version of inorder, postorder 
or preorder.

I did it with a BFS. 

It took me about 1 hour to ditch trying to
compare and write the iterative tree traversal.

It took me about 10 minutes  to write this approach.

I think the way i've designed it is really good. In my
other approach, I was trying was to iterate through the 2
trees at the same time. I am essentially doing the same 
thing here, only that it's a lot cleaner.
"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def same_node(p: "TreeNode", q: "TreeNode") -> bool:
    if p is None and q is None:
        return True
    elif p is not None and q is None:
        return False
    elif p is None and q is not None:
        return False
    elif p is not None and q is not None:
        return p.val == q.val


def bfs(node):

    queue = list()
    index = 0
    queue.append(node)
    queue_length = 1

    while index < queue_length:

        current = queue[index]

        if current is not None:
            queue.append(current.left)
            queue.append(current.right)
        queue_length = len(queue)
        index += 1

        yield current


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        tree1 = bfs(p)
        tree2 = bfs(q)
        for node1, node2 in zip(tree1, tree2):
            if not same_node(node1, node2):
                return False

        return True
