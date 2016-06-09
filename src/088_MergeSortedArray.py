#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on Jun 9, 2016
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. 
The number of elements initialized in nums1 and nums2 are m and n respectively.
@author: frank.he
'''
class Solution:
    def mergeSortedArray(self, a1, a2):
        len1 = len(a1)
        len2 = len(a2)
        while len1!=0   