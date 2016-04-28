'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

UPDATE (2016/2/13):
The return format had been changed to zero-based indices. Please read the above updated description carefully. 
Created on Apr 27, 2016

@author: marpe
'''
class Solution:
    def twoSum(self, num, target):
        nums = num
        for ind1,val in enumerate(nums):
            if target - val in nums:
                return ind1, num.index(target - val)
            
            
if __name__ == '__main__':
    print (Solution().twoSum([2,3,4],7))