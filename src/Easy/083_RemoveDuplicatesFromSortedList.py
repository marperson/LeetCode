#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on Jun 9, 2016
 Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3. 
@author: frank.he
'''

class Solution:
    def removeDuplicates(self,list):
        node = None
        while list.next != None:
            if list.next.value == node:
                list.next = list.next.next
            else:
                node = list.value
            
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head == None or head.next == None:
            return head
        p = head
        while p.next:
            if p.val == p.next.val:
                p.next = p.next.next
            else:
                p = p.next
        return head