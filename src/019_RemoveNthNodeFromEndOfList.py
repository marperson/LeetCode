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
from src.basic import LinkedList
class Solution(LinkedList):
    
    def removeNode(self, n, head):
        p1 = head
        p2 = head
        
        for i in range(n):
            p1 = p1.next
       
        
        while (p1 != None):
            p1 = p1.next
            p2 = p2.next
            
        p2.next = p2.next.next
        return head
    
 
# Build Liked list
node1 = LinkedList('1', None)
node2 = LinkedList('2', None)
node3 = LinkedList('3', None)

node1.next = node2
node2.next = node3

# print (node2.getNext().getData())

# Remove node
myList = Solution().removeNode(2, node1)
# myList.LinkedList.printList(node1)
