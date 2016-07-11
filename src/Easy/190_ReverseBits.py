#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in 
binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?

Related problem: Reverse Integer
'''

class Solution:
    # @param v, integer
    # @return integer
    
    def reverse(self,v):
        b=0
        #b = format(v,'b')
        # b = bin(v)
        # remove first '0b' symbol
        # b = b[2::1]
        '''  
    {} places a variable into a string
    0 takes the variable at argument position 0
    : adds formatting options for this variable (otherwise it would represent decimal 6)
    031 formats the number to eight digits zero-padded on the left
    b converts the number to its binary representation

        '''
        b = "{0:031b}".format(v)
        #print (int(b,2))
        print (b)
        b = b[::-1]
        print (b)
        b = int(b,base=2)
        #b = str(b).fromBinaryToInt()
        return b
        
        
        
    '''
   思路二

按位处理，将输入n的二进制表示从低位到高位的值依次取出，逆序排列得到翻转后的值。这里更新res的时候，用纯位操作会比用加法要快的多。

'''
    # @param n, an integer
    # @return an integer
    def reverseBits2(self, n):
        ans = 0
        for i in range(32):
            ans <<= 1
            ans |= n & 1
            n >>= 1
        return ans
    
    '''
思路一

先将输入转换成2进制字符串，再翻转并扩充到32位，再将此32位的二进制转为无符号整数即可。利用Python的bin()函数很方便。
    '''
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        b = bin(n)[:1:-1]
        print (b)
        return int(b + '0'*(32-len(b)), 2)

s = Solution()
print(s.reverseBits(43261596))
