'''
Created on Apr 20, 2016
current node value should be superior than previous node
@author: frank.he
'''

class Solution:
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