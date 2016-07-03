#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on Jun 5, 2016
Given an array and a value, remove all instances of that value in place and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:
Given input array nums = [3,2,2,3], val = 3

Your function should return length = 2, with the first two elements of nums being 2.

Hint:

    Try two pointers.
    Did you use the property of "the order of elements can be changed"?
    What happens when the elements to remove are rare?
    
    
解题思路：去掉数组中等于elem的元素，返回新的数组长度，数组中的元素不必保持原来的顺序。使用头尾指针，头指针碰到elem时，与尾指针指向的元素交换，将elem都换到数组的末尾去。

@author: marpe
'''

class Solution:
    def removeElement(self, A, number):
        B = []
        # for i in A does NOT work, it starts from A[1]
        for i in range(0, len(A)):
            if A[i] != number:
                B.append(A[i])
                print (B)
        print(B)       
        return len(B)
     
     
print (Solution().removeElement([1,2,2,3,4,4],2))       
        
