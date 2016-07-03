#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its level order traversal as:

[
  [3],
  [9,20],
  [15,7]
]

解题思路：二叉树的层序遍历可以用bfs或者dfs来实现。这里使用的dfs实现，代码比较简洁。实际上，二叉树的先序遍历就是dfs实现。

　　　　   比如一棵树如下：

　　　　　　　　　　　　　　　　1

　　　　　　　　　　　　　　　/　  \

　　　　　　　　　　　　　　 2       3

　　　　　　　　　　　　　 /    \    /   \

　　　　　　　　　　　　　4     5  6    7

　　　　    二叉树的先序遍历为{1，2，4，5，3，6，7}，可以看到这个遍历顺序实际上就是dfs。在这个遍历中，我们可以用一个level来记录节点的高度，根节点高度为0。

'''
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def preorder(self, root, level, res):
        if root:
            if len(res) < level+1: 
                res.append([])
            res[level].append(root.val)
            self.preorder(root.left, level+1, res)
            self.preorder(root.right, level+1, res)
    def levelOrder(self, root):
        res=[]
        self.preorder(root, 0, res)
        return res
