#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3

begin to intersect at node c1.

Notes:

    If the two linked lists have no intersection at all, return null.
    The linked lists must retain their original structure after the function returns.
    You may assume there are no cycles anywhere in the entire linked structure.
    Your code should preferably run in O(n) time and use only O(1) memory.
思路一：

如果有相交，那么他们相交点之后的节点肯定都是共有的，然后两个链表有长有短的话，
就先把长的读到和短的一样长，然后两个人在同时走，走到第一个相同的点就是答案了。如果相同的点是NULL了，那就是没有相交点。


如果有一个链表为空，返回NULL；先遍历链表得到A、B的长度，如果最后一个节点不同，返回NULL；使长的链表先走长度差步，然后一起往后走，直到节点相同返回即可。

'''
# Definition for singly-linked list.  
# class ListNode:  
#     def __init__(self, x):  
#         self.val = x  
#         self.next = None  
  
class Solution:  
    # @param two ListNodes  
    # @return the intersected ListNode  
    def getIntersectionNode(self, headA, headB):  
        if headA == None or headB == None:  
            return None  
          
        lenA = 1  
        hA = headA  
        while hA.next != None:  
            lenA += 1  
            hA = hA.next  
              
        lenB = 1  
        hB = headB  
        while hB.next != None:  
            lenB += 1  
            hB = hB.next  
          
        if hA != hB:  
            return None  
          
        hA = headA  
        hB = headB  
        if lenA > lenB:  
            for i in range(lenA - lenB):  
                hA = hA.next  
        else:  
            for i in range(lenB - lenA):  
                hB = hB.next  
          
        while hA != hB:  
            hA = hA.next  
            hB = hB.next  
          
        return hA  