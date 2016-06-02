#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on May 29, 2016

@author: marpe
'''

class Solution():
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            print('Empty String')
        elif len(strs) == 1:
            print('Only one String in the list')
        else:
            for i in range(1, len(strs)):
                # Call compareStr method to compare two strs
                strs[0] = self.compareStr(strs[0], strs[i])
                # print (strs[0])
        
        return strs[0]
    
    def compareStr(self, a, b):
        sameStr = ''
        i = 0
        while i < min(len(a), len(b)):
            if a[i] == b[i]:
                sameStr += a[i]
            else:
                break
            i += 1
        return sameStr
    

print (Solution().longestCommonPrefix(['abc', 'ab']))
