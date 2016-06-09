#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on Jun 8, 2016
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example,
Given s = "Hello World",
return 5. 
@author: frank.he
'''
class Solution:
    def lengthOfLastWord(self,s):
        newStr = s[::-1]
        str = ''
        for i in newStr:
            if i != ' ':
                str = str+i
            else:
                break
        if not str:
            return 0
        else:
            return len(str)
        
    def lengthOfLastWord2(self, s):
        return len(s.split()[len(s.split())-1]) if s.split() != [] else 0

print(Solution().lengthOfLastWord(''))