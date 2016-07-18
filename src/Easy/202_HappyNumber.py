'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its 
digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. 
Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

    12 + 92 = 82
    82 + 22 = 68
    62 + 82 = 100
    12 + 02 + 02 = 1


@author: marpe
'''

class Solution:
    # @param n, positive integer number
    # @return boolean
    
    def isHappyNumber(self, n):
        l = list(str(n))
        sum = 0
        n = 0
        while sum != 1 and n < 10000:
            sum = 0
            for i in l:
                sum += int(i) ** 2
            print (l)
            print (sum)
            l = list(str(sum))
            n += 1
        if n < 10000:
            return True
        else :
            return False
    
s = Solution()
print (s.isHappyNumber(20))
        
