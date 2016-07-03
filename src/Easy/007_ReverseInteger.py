"""
Reverse digits of an integer.
Example1: x = 123, return 321
Example2: x = -123, return -321
"""
__author__ = 'Frank He'

class Solution:
    def reverseInteger(self, num):
        sign = -1 if num < 0 else 1
        num = abs(num)
        x = 0
        while int(num) > 0:
            x = int(x * 10 + num % 10)
            num /= 10
        return x * sign
    
    def reverseIntegerString(self, num):
        # Remove leading zero
        while num > 0:
            if num % 10:
                num /= 10
            else:
                break
        
        s = str(num)
        l = list(num)
        print(l)



print(Solution().reverseInteger(123))
#test = Solution().reverseIntegerString(123)
