'''
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Created on Jun 18, 2016

@author: marpe
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class MaximumDepthOfBinarySearchTree:
    def preOrder(self,node,dep):
        if node:
            if 
            dep++
            self.preOrder(node.leftChild, dep+1)
            self.preOrder(node.rightChild, dep+1)
        
        
    def depth(self,root):
        dep = 0;
        self.preOrder(root,0)
        
    """
    @param root: The root of binary tree.
    @return: An integer
    """ 
    def maxDepth(self, root):
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1   