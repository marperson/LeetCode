'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display
this pattern in a fixed font for better legibility)
P   A   H   N   1   5   ...
A P L S I I G   2 4 6 8 ...
Y   I   R       3   7   ...
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

@author: frank.he
'''
class Solution:

    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    # @good coding!
    def convert(self, s, nRows):
        #If nRow==1, then return s
        if nRows == 1:
            return s
        # Create a list with nRows elements, "Paypayishiring" with nRow==3, list with three elements
        tmp = ['' for i in range(nRows)]
        #Default value
        index = -1; step = 1
        #Iteration vertically 
        for i in range(len(s)):
            index += step
            if index == nRows:
                index -= 2; step = -1
            elif index == -1:
                index = 1; step = 1
            tmp[index] += s[i]
        return ''.join(tmp)


#if __name__ == '_main__':
print (Solution().convert('Paypayishiring', 4))
