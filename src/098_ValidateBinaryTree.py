#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on Apr 20, 2016
current node value should be superior than previous node
����������Ƚϵ�ǰ���ֵ�Ƿ����ǰһ���ֵ����
@author: frank.he
'''
from src.basic import BinarySearchTree

class Solution(BinarySearchTree):
    '''
    # @param root, a tree node
    # @return a boolean
    
    val = None
    def isValidBST(self, root):
        if root is None: 
            return True
        res = self.isValidBST(root.left)
        if self.val is None:
            self.val = root.val
        else:
            res = res and (root.val > self.val)
            self.val = root.val
        res = res and self.isValidBST(root.right)
        return res
    '''

        
    def isValidateBST(self, root):
        if self.root is None:
            return True
        else:
            if self.leftChild > root and self.rightChild < root:
                return False
            return self.isValidateBST(self.leftChild) and self.isValidateBSI(self.rightChild)


bst = BinarySearchTree(2)
bst.insert(3)
bst.insert(4)       
print (bst.isValidateBST(2))       