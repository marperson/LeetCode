#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on Jun 2, 2016
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
解题思路：判断括号匹配的合法性。使用一个栈来解决问题。遇到左括号入栈，遇到右括号，检查栈顶的左括号是否匹配，
如果匹配，弹栈，如果不匹配，返回错误。如果栈为空，而遇到右括号，同样返回错误。遍历完后，栈如果不空，同样返回错误。
@author: frank.he
'''


class Solution:
    
    def validateParentheses1(self, str):
        stack = []
        pushChars = '<({['
        popChars = '>)}]'
        
        for c in str:
            if c in pushChars:
                stack.append(c)
            elif c in popChars:
                # validate stack length, avoid this kind of string '(}>)' forces pop empty stack
                if not len(stack):
                    return False
                if stack.pop() != pushChars[popChars.index(c)]:
                    return False
            else:
                    return False
                
        return True
    
    
    def validateParentheses2(self, str):
        stack = []
        
        for s in str:
            if s == '(' or s == '[' or s == '{':
                stack.append(s);
                print (len(stack))
            elif s == ')':
                #Validate stack is not empty, otherwise it causes exception
                if len(stack) == 0 or stack.pop() != '(':
                    return False
            elif s == ']':
                if len(stack) == 0 or stack.pop() != '[':
                    return False
            elif s == '}':
                if len(stack) == 0 or stack.pop() != '{':
                    return False
            else:
                return False
            
        # validate stack is empty at the end
        if len(stack) != 0:
            return False
        
        # If all above conditions are not met, return true
        return True
            
        

str = '{{(())}}'
print (Solution().validateParentheses2(str))
                
                
        
    
