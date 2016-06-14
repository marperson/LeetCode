#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value. 
Created on Jun 9, 2016
这题比较简单。用递归来做。首先判断两个根节点的值是否相同，如果相同，递归判断根的左右子树。
@author: marpe
'''
from src/Basic import BinarySearchTree
class Solution(BinarySearchTree):
    # @Param: root1, tree 1 root node
    # @param: root2, tree 2 root node
    # return True or False
    
    def isSameTree(self,root1, root2):
        if root1 is None or root2 is None:
            print ('tree is empty)
        else:
            # Left Nodes
            if not root1.leftChild is None and root2.leftChild is None:
                return False
            elif root1.leftChild is None and not root2.leftChild is None:
                return False
            elif not root1.leftChild is None and not root2.leftChild is None:  
                isSameTree(root1.leftChild, root2.leftChild)
            elif root1.leftChild is None and root2.leftChild is None:
                if root1 != root2:
                    return False
            # Right Nodes
            if not root1.rightChild is None and root2.rightChild is None:
                return False
            elif root1.rightChild is None and not root2.rightChild is None:
                return False
            elif not root1.rightChild is None and ot root2.rightChild is None:  
                isSameTree(root1.rightChild, root2.rightChild)
            elif root1.rightChild is None and root2.rightChild is None:
                if root1 != root2:
                    return False
        return True
    
    def isSameTree2(self, p, q):
        if p == None and q == None: return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False
    
    
        
# Definition for a  binary tree node  
# class TreeNode:  
#     def __init__(self, x):  
#         self.val = x  
#         self.left = None  
#         self.right = None  
      
class Solution:  
    # @param p, a tree node  
    # @param q, a tree node  
    # @return a boolean  
    def isSameTree(self, p, q):  
        if p is None and q is None:  
            return True  
        elif p is None or q is None:  
            return False  
        else:  
            if p.val == q.val:  
                if self.isSameTree(q.left,p.left):  
                    return self.isSameTree(p.right,q.right)  
            return False  