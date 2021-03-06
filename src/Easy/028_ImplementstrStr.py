#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on Jun 5, 2016
Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack. 

题意：实现字符串匹配函数，并返回一个指针，这个指针指向原字符串中第一次出现待匹配字符串的位置。
如：haystack='aabbaa'; needle='bb'。如果使用python实现，则最后返回的应该是一个字符串，即：'bbaa'。

解题思路：这道题我是使用KMP算法写的，到现在KMP算法都不是很懂，只是按照《算法导论》上的伪代码机械的实现了一遍。

@author: marpe
'''

class Solution:
    def strStr(self, source, target):
        if source is None or target is None:
            return -1
        len_s = len(source)
        len_t = len(target)
        for i in range(len_s - len_t + 1):
            j = 0
            while (j < len_t):
                if source[i + j] != target[j]:
                    break
                print (j)
                j += 1
            if j == len_t:
                return i
        return -1
     
     
print (Solution().strStr('aabbcc','b'))