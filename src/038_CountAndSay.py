#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on Jun 8, 2016
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n, generate the nth sequence.
Note: The sequence of integers will be represented as a string. 
1     ->    11, one one
11    ->    21, two one
12    ->    1112, one one and one two
21    ->    1211, one two and one one
@author: frank.he
'''

class Solution:
    def countAndSay(self, n):
        if n == 1:
            return '1'
        elif n ==2:
            return '11'        
        else:
            str = '11'
            for i in range(n-2):
                s= ''
                for j in range(int(len(str) / 2)):
                    tmp = str[(2*j):(2*j+2):2] + str[(2*j + 1):(2*j+2+1):2]
                    if tmp == '11':
                        s += '21'
                    elif tmp == '12':
                        s += '1112'
                    elif tmp == '21':
                        s += '1211'
                str = s              
        return str
    
     # @return a string
    def count(self,s):
        t=''; count=0; curr='#'
        for i in s:
            if i!=curr:
                if curr!='#':
                    t+=str(count)+curr
                curr=i
                count=1
            else:
                count+=1
        t+=str(count)+curr
        return t
    def countAndSay2(self, n):
        s='1'
        for i in range(2,n+1):
            s=self.count(s)
        return s
                

print (Solution().countAndSay(6))
