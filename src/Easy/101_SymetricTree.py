#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3


Bonus points if you could solve it both recursively and iteratively. 
Created on Jun 11, 2016
解题思路：这题也不难。需要用一个help函数，当然也是递归的。当存在左右子树时，判断左右子树的根节点值是否相等，
如果想等继续递归判断左子树根的右子树根节点和右子树根的左子树根节点以及左子树根的左子树根节点和右子树根的右子树根节点的值是否相等。
然后一直递归判断下去就可以了。
@author: marpe
'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def symmetricTree(self,root):
        if root is None:
            print ('Tree is empty')
        else:
            if root.leftChild and root.rightChild:
                if root.leftChild!=root.rightChild:
                    return False
                self.symmetricTree(root.leftChild)
                self.symmetricTree(root.rightChild)
    # @param root, a tree node
    # @return a boolean
    def help(self, p, q):
        if p == None and q == None: return True
        if p and q and p.val == q.val:
            return self.help(p.right, q.left) and self.help(p.left, q.right)
        return False
    
    def isSymmetric(self, root):
        if root:
            return self.help(root.left, root.right)
        return True           
        