'''
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
'''
from _ast import Str


class Solution:
    # @param s, string
    # @return integer
    def column(self, s):
        str = list(s)
        # x for x in s:
        
        x = 0
        control=0
        for i in str[::-1]: 
            y = ord(i) - ord('A') + 1
            print (y)
            y *= 26**control
            x =x+ y
            control +=1
            print (x)
            
        return x
            
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        ans = 0
        for e in s:
            ans = ans * 26 + ord(e) - ord('A') + 1
        return ans        
        
        

s = Solution()
print (s.titleToNumber('ZZ'))
