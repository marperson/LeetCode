'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its bottom-up level order traversal as:

[
  [15,7],
  [9,20],
  [3]
]

'''

class BinaryTreeLevelOrderTraversalII:
    def preOrder(self,node,level,res):
        if node:
            if len(res) < level+1:
                res.append([])
            res[level].append(node.val)
            self.preOrder(node.leftChild, level+1, res)
            self.preOrder(node.rightChild, level+1, res)
                
        
    def count(self,root):
        res = []
        self.preOrder(root, 0, res)
        return res.reverse()
