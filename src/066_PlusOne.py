#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on Jun 9, 2016
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.
给定一个数组，这个数组代表一个数字，数字的最高位存在数组最前面，数字的最低位存在数组的最后面（符合书写习惯），输出该数字加1得到的数组

例如 input:[9,9] output:[1,0,0]
这只一个flag标志位就可以了。

思路
从数组的最低位开始遍历，若该位加一（这个1包含了进位的1和最开始的加的1）不产生进位的话，将该位加一
返回结果即可，若该位产生进位，则将该位置为0，继续遍历即可，但要注意类似999+1=1000这种数组位数增加的情况，此时将最高位置为0然后在数组最前面加个1即可
@author: frank.he
'''

class Solution:
    def plusOne(self,list):
        length = len(list) -1
        num=0
        for i in list:
            num = num+i*(10**length)
            length = length -1
        newList=[]
        for i in str(num+1):
            newList.append(i)
        return newList
    
    def plusOne2(self, digits):
        flag = 1
        for i in range(len(digits)-1, -1, -1):
            if digits[i] + flag == 10:
                digits[i] = 0
                flag = 1
            else:
                digits[i] = digits[i] + flag
                flag = 0
        
        if flag == 1:
            digits.insert(0, 1)
        return digits

print (Solution().plusOne([9,0,0]))