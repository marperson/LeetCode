'''
Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37.45

Credits:
Special thanks to @ts for adding this problem and creating all test cases.

Subscribe to see which companies asked this question

'''

class Solution:
    # @param v1, a string
    # @param v2, a string
    # @return a boolean
    def compare(self, v1, v2):
        v1Arr = v1.split(".")
        v2Arr = v2.split(".")

        len1 = len(v1Arr)
        len2 = len(v2Arr)
        
        lenMax = max(len1, len2)
        
        for x in range(lenMax):
            v1Token = 0
            if x < len1:
                v1Token = int(v1Arr[x])
            
            v2Token = 0
            if x < len2:
                v2Token = int(v2Arr[x])

            if v1Token > v2Token:
                return 1
            if v1Token < v2Token:
                return -1
        return 0

        
        
s = Solution()
print (s.compare('2.1.4', '1.1.3.4'))
# Can not use compare(1.1, 0.1.3) as it would be considered as integer
