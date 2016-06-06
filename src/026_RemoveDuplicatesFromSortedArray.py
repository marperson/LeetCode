#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on Jun 5, 2016
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.
解题思路：使用一个指针j，当i向后遍历数组时，如果遇到与A[j]不同的，将A[i]和A[j+1]交换，同时j=j+1，即j向后移动一个位置，然后i继续向后遍历s
@author: marpe
'''
class Solution:
    # below methods work because it's a SORTED ARRAY
    def removeDuplicates(self, A):
        if len(A) == 0:
            return 0
        j = 0
        for i in range(0, len(A)):
            if A[i] != A[j]:
                # Fast way to swap A[i] and A[j+1]
                # A[i], A[j+1] = A[j+1], A[i]
                tmp = A[j + 1]
                A[j + 1] = A[i]
                A[i] = tmp
                j = j + 1
        return j + 1
    
    def removeDuplicates2(self, array):
        B = []
        before = None
        # coutb = 0
        for number in array:
            if before != number:
                B.append(number)
                before = number
                # countb = 1
            '''
            elif coutb < 2:
                B.append(number)
                coutb += 1
            '''
        p = 0
        for number in B:
            # Reassign values to array
            # array[p] = number
            
            # Count the difference
            p += 1
        
        print (B)
        return p
                

          
        
print (Solution().removeDuplicates2([1, 2, 2, 4, 27, 27, 30, 30]))
