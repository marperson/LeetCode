'''
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 

Credits:
'''

class Solution:
    # @param num, positive integer input
    # @param return string
    def title(self, num):
        str = ''
        x = num
        flag = False
        while x != 0:
            if int(x % 26) !=0:
                str += chr(ord('A') + int(x % 26) - 1)
            elif int(x%26) == 0 and x >26:
                str += chr(ord('A'))
            elif num ==26:
                str += chr(ord('Z'))
                #x+=1
            # str1 += chr(ord('A') + int(x/26) - 1)
            print (x, str)
           
            x = int (x / 26)
            flag = True
        return str[::-1]

    def convertToTitle(self, num):
        ans = ''
        while num:
            ans = chr(ord('A') + int((num - 1) % 26)) + ans
            num = int((num - 1) / 26)
        return ans
    
    
s = Solution()
print (s.convertToTitle(108))
