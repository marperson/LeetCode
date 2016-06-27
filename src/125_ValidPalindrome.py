#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
 Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome. 
解题思路：将不是字母的字符去掉，然后转换成小写，然后简单的回文判断。
'''

class Solution:
    def isPalindrome(self, s):
        str = ''
        if s == '':
            return False
        else:
            # remove space
            s = s.replace(' ', '')
            # validate only alpha and digit
            for i in range(0, len(s)):
                if s[i].isalpha or s[i].isdigit:            
                    # convert to lower cases
                    str += s[i].lower()
            print (str)
    
            for i in range(0, int(len(s) / 2)):
                    if s[i] != s[len(s) - i - 1]:
                        return False
                    
            return True
    
str = 'a man a plan a canal panama'
print (Solution().isPalindrome(str))

print (' '.isalpha())
