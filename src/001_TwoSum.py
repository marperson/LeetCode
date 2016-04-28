'''
"""
Given an array of integers, find two numbers such that they add up to a specific target number.
The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be
less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution.
Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
"""
__author__ = 'Danyang'

@author: marpe
'''
class Solution:
    def twoSum(self, num, target):
        """
        built-in method .index
        :param num: list
        :param target: int
        :return: tuple, (index1, index2)
        """
        for ind1, val1 in enumerate(num):
            val2 = target - val1
            if val2 in num:
                ind2 = num.index(val2)
                if ind1 != ind2:
                    if ind1 > ind2:
                        return ind2 + 1, ind1 + 1
                    elif ind1 < ind2:
                        return ind1 + 1, ind2 + 1
    def towSumHashMap(self, num, target):
        hash_map = {}
        for ind, val in enumerate(num):
            hash_map[val] = ind
            
        
        for ind1, val in enumerate(num):
            if target - val in hash_map:
                ind2 = hash_map[target-val]
                if ind1 !=ind2:
                    if ind1 > ind2:
                        return ind2+1, ind1+1
                    else:
                        return ind1+1, ind2+1
    '''
     def towSumHashMap(self, num, target):
        hash_map = {}
        for ind, val in enumerate(num):
            hash_map[val] = ind
        
        for ind1, val in enumerate(num):
            if target - ind1 in hash_map:
                return ind1, num.index(target - ind1)           
    '''    
            
if __name__ == '__main__':
    print (Solution().twoSum([1, 2, 4, 7], 4))
    print (Solution().towSumHashMap([2, 2, 4, 7], 4))