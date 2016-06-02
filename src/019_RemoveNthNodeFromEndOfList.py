#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on Jun 1, 2016
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.
Try to do this in one pass. 


这道题的含义是删除链表的倒数第n个节点。

解题思路：加一个头结点dummy，并使用双指针p1和p2。p1先向前移动n个节点，然后p1和p2同时移动，当p1.next==None时，此时p2.next指的就是需要删除的节点。

@author: frank.he
'''

class Solution:
    def removeNode(self, n):