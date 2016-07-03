#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on May 29, 2016
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
解题思路：将罗马数字转换成对应的整数。首先将罗马数字翻转，从小的开始累加，如果遇到CM（M-C=1000-100=900）这种该怎么办呢？因为翻转过来是MC，M=1000先被累加，
所以使用一个last变量，把M记录下来，如果下一个数小于M，那么减两次C，然后将C累加上，这个实现比较巧妙简洁。

Roman number chart
http://literacy.kent.edu/Minigrants/Cinci/romanchart.htm


@author: marpe
'''

class Solution:
    def romanToInteger(self, roman):
        # create a dictionary
        chart = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        # Create a list
        reverseRoman = roman[::-1]
        sum = 0
        last = 0
        sign = 1
        for word in reverseRoman:
            # Compare last value with current value
            if last < chart[word]:
                sum += chart[word]
                sign = 1
                last = chart[word]
            elif last > chart[word]:
                sum -= chart[word]
                sign = -1
                last = chart[word]
            # When two same letters appear, identify it positive or negative
            else:
                sum += sign * chart[word]              

        return sum
        
        



print (Solution().romanToInteger('MXXVII'))
print (Solution().romanToInteger('CCM'))
