#!/usr/bin/python
# -*- coding: utf-8 -*-


'''
Created on Jun 3, 2016
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
合并两个有序链表
思路：依次比较两个链表的当前元素的val值，p指向小的那个，同时小的那个指针后移。注意链表为空的情况，指针后移出现一个为空时跳出循环，在下面的if判断是哪个还不为空则将p指向它那一串即可。
@author: frank.he
'''
from src.basic import LinkedList
class Solution(LinkedList):
    def mergeTwoSortedLists(self, list1, list2):
     list = LinkedList()
        
        while list1 != None and list2 != None:
            if list1.value < list2.value:
                list.next = list1
                list1 = list1.next
            else:
                list.next = list2
                list2 = list2.next
                
        if list1 == None:
            list.next = list2
            list2 = list2.next
        
        if list2 == None:
            list.next = list1
            list1 = list1.next
        return list.next
        

node1 = LinkedList(0)
node2 = LinkedList(0)
node1.setData(5)
node1.next = node2

        
        
        
