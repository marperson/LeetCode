'''
Created on May 29, 2016
Determine whether an integer is a palindrome. Do this without extra space.

16461 -> reverse is th same

click to show spoilers.
Some hints:

Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.


@author: marpe
'''
class Solution:
    def PalindromeNumber(self, num):
        newNum = 0
        originalNum = num
        while num != 0:      
            newNum*=10  
            tmp = num%10
            num = int(num/10)    
            newNum+=tmp

            print (newNum)
        if newNum == originalNum:
            return True
        else:
            return False
        
        
print (Solution().PalindromeNumber(16451))
    