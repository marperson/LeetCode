'''
Created on Jun 9, 2016
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100". 
@author: frank.he
'''

class Solution:
    # @param {string} a a number
    # @param {string} b a number
    # @return {string} the result
    def addBinary(self, a, b):
        indexa = len(a) - 1
        indexb = len(b) - 1
        carry = 0
        sum = ""
        while indexa >= 0 or indexb >= 0:
            x = int(a[indexa]) if indexa >= 0 else 0
            y = int(b[indexb]) if indexb >= 0 else 0
            if (x + y + carry) % 2 == 0:
                sum = '0' + sum
            else:
                sum = '1' + sum
            carry = (x + y + carry) / 2
            indexa, indexb = indexa - 1, indexb - 1
        if carry == 1:
            sum = '1' + sum
        return sum
        
    
    def addBinary2(self, a, b):
        aIndex = len(a)-1; bIndex = len(b)-1
        flag = 0
        s = ''
        while aIndex>=0 and bIndex>=0:
            num = int(a[aIndex])+int(b[bIndex])+flag
            flag = num/2; num %= 2
            s = str(num) + s
            aIndex -= 1; bIndex -= 1
        while aIndex>=0:
            num = int(a[aIndex])+flag
            flag = num/2; num %= 2
            s = str(num) + s
            aIndex -= 1
        while bIndex>=0:
            num = int(b[bIndex])+flag
            flag = num/2; num %= 2
            s = str(num) + s
            bIndex -= 1
        if flag == 1:
            s = '1' + s
        return s
    
    def addBinary3(self, a, b):
        length = max(len(a),len(b)) + 1
        sum = ['0' for i in range(length)]
        if len(a) <= len(b):
            a = '0' * ( len(b) - len(a) ) + a
        if len(a) > len(b):
            b = '0' * ( len(a) - len(b) ) + b
        flag = 0
        i = len(a) - 1
        while i >= 0:
            if int(a[i]) + int(b[i]) + flag == 3:
                sum[i+1] = '1'
                flag = 1
            elif int(a[i]) + int(b[i]) + flag == 2:
                sum[i+1] = '0'
                flag = 1
            elif int(a[i]) + int(b[i]) + flag == 1:
                sum[i+1] = '1'
                flag = 0
            else:
                sum[i+1] = '0'
                flag = 0
            i = i - 1
        if flag == 1:
            sum[0] = '1'
        if flag == 0:
            sum = sum[1:length]
        sum = ''.join(sum)
        return sum
print(Solution().addBinary('11', '100'))     