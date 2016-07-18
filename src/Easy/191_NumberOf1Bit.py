#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).
For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.
'''


class Solution:
    def bit(self,i):
        a = "{0:032b}".format(i)
        count = 0
        b = list(a)

        for i in range(len(b)):
            print(b[i])
            # b is string list, so can not use b[i] == 1
            if b[i]=='1':
                count +=1
            
                
        return count
                
        
        
        
a = Solution()
print (a.bit(11))