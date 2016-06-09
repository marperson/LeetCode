#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on Jun 4, 2016
 Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed. 

解题思路：这题主要涉及到链表的操作，没什么特别的技巧，注意不要出错就好。最好加一个头结点，操作起来会很方便。
@author: marpe
'''


class Solution:
    #method 1
    def swapNodesInPairs(self,head):
        pre = list(0)
        pre.next = head
        current = head
        head = pre
        while current and current.next:
            #Set new list order
            pre.next = current.next
            current.next = pre.next.next
            #Set new list values
            pre.next.next = current
            pre = current
            current = current.next
        return head.next    
    # method 2
    def swapPairs(self, head):
        # Write your code here
        if head == None or head.next == None:
            return head
        dummy = list(0); dummy.next = head
        p = dummy
        while p.next and p.next.next:
            tmp = p.next.next
            p.next.next = tmp.next
            tmp.next = p.next
            p.next = tmp
            p = p.next.next
        return dummy.next            
        
