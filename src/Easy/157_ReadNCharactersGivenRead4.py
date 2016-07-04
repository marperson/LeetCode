#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on Jul 3, 2016
The API: int read4(char *buf) reads 4 characters at a time from a file.
The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.
By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.

Note:
The read function will only be called once for each test case.


Hint:
Consider which one is smaller, read4(buf) or n - num.
@author: marpe
题目意思是给你一个read4的函数，实现一个readn的函数。

一开始题目一直没搞懂，原来，read4(buf) 是指，读4个字符存到buf，或者读剩下的不足四个的字符，返回的数字是存到buf里的字符数。
需要注意的是，跳出while后，需要判断读的数字是不是超过n了，因为我们只实现readn，要返回的数字最多就是n，存到buf里的也最多是n个字符。

所以如果cnt大于n了，那么buf里面就要将buf[n]设置为末尾也就是‘\0’

顺便提下，memcpy在<string.h>头文件里，是c的，应该可以用strncpy代替
'''

# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution:
    # @param buf, Destination buffer (a list of characters)
    # @param n,   Maximum number of characters to read (an integer)
    # @return     The number of characters read (an integer)
    def read(self, buf, n):
        numBytes = 0
        
        while n > 0:
            buf4 = [None] * 4
            size = read4(buf)
            minLen = min(size, n - numBytes)

            if minLen == 0:
                return numBytes
            
            for i in range(minLen):
                buf[numBytes] = buf4[i]
                numBytes += 1
        
        return numBytes
    
    
    
#Solution 2
# Time:  O(n)
# Space: O(1)
#
# The API: int read4(char *buf) reads 4 characters at a time from a file.
# 
# The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.
# 
# By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.
# 
# Note:
# The read function may be called multiple times.
#

# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
def read4(buf):
    global file_content
    i = 0
    while i < len(file_content) and i < 4:
        buf[i] = file_content[i]
        i += 1
    
    if len(file_content) > 4:
        file_content = file_content[4:]
    else:
        file_content = ""
    return i
        
# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution2(object):
    def __init__(self):
        self.__buf4 = [''] * 4
        self.__i4 = 0
        self.__n4 = 0
        
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        i = 0
        while i < n:
            if self.__i4 < self.__n4:  # Any characters in buf4.
                buf[i] = self.__buf4[self.__i4]
                i += 1
                self.__i4 += 1
            else:
                self.__n4 = read4(self.__buf4)  # Read more characters.
                if self.__n4:
                    self.__i4 = 0
                else:  # Buffer has been empty.
                    break
        
        return i

if __name__ == "__main__":
    global file_content
    sol = Solution()
    buf = ['' for _ in xrange(100)]
    file_content = "ab"
    print buf[:sol.read(buf, 1)]
print buf[:sol.read(buf, 2)] 