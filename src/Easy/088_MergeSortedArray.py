#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on Jun 9, 2016
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. 
The number of elements initialized in nums1 and nums2 are m and n respectively.
解题思路：归并排序的归并这一步的实现，原理很多地方都有。使用一个tmp临时数组进行归并
@author: frank.he
'''
class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        tmp = [0 for i in range(m + n)]
        i = 0; j = 0; k = 0
        while i < m and j < n:
            if A[i] <= B[j]:
                tmp[k] = A[i]; i += 1
            else:
                tmp[k] = B[j]; j += 1
            k += 1
        if i == m:
            while k < m + n:
                tmp[k] = B[j]; k += 1; j += 1
        else:
            while k < m + n:
                tmp[k] = A[i]; i += 1; k += 1
        for i in range(0, m + n):
            A[i] = tmp[i]
               
    #@param A: sorted integer array A which has m elements, 
    #          but size of A is m+n
    #@param B: sorted integer array B which has n elements
    #@return: void
    def mergeSortedArray(self, A, m, B, n):
        for i in range(n):
            A[i+m] = B[i]
        A.sort()
    
    def mergeSortedArray2(self,a1,a2):
        len1 = len(a1)
        len2 = len(a2)
        # Create a initial list
        tmp = [ 0 for i in range(len1+len2)]
        
        # Assign a1 to tmp
        for i in range(len1):
            tmp[i] = a1[i]
        
        # Assign a2 to tmp
        for i in range(len2):
            tmp[len1+i] = a2[i]

        # Sort and return
        tmp.sort()
        return tmp
        # can not use 'return tmp.sort()' 
        
        

a1 = [1,3,5,6]
a2 = [2,4,6,7]
print (Solution().mergeSortedArray2(a1, a2))
