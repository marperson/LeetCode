#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on Apr 20, 2016
将abc def形式的字符串翻转成def abc，并且去掉多余的空格。
先将这个字符串翻转过来，再逐次翻转每个词。（当然不是效率最高的办法，只是为了好写。）
@author: frank.he
'''

class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        return ' '.join(word[::-1] for word in s[::-1].split())
    '''
        newStr=''
        for word in s[::-1]:
            newStr+=word
        return newStr
    '''
    '''    extended slice [begin:end:step]
           split() change string to a list with seperate words
           '''

str = "This is word"
s = Solution()
#print (s.reverseWords(str))
print(s.reverseWords(str))

#print (str[::-1].split())