'''
189. Rotate Array

    Total Accepted: 79814
    Total Submissions: 365066
    Difficulty: Easy

Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

[show hint]

Related problem: Reverse Words in a String II
'''

class Solution:
    # @param l, input array
    # @param k, integer 
    # @return array
    def rotate(self,l,k):
        newList = []
        if len(l)<k:
            print ('Array length is less than "k"')
            return 0
        elif len(l)==k:
            print ('Rotate whole array')
            return l
        else:
            newList = l[k+1::1]
            for i in range(k):
                newList.append(l[i])
            print (newList)
            
s=Solution()
l = [1,2,3,4,5,6,7]
s.rotate(l, 3)
            
