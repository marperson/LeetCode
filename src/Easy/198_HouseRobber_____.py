#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, 
the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and 
it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum 
amount of money you can rob tonight without alerting the police.
解题思路：

动态规划（Dynamic Programming）

状态转移方程：

dp[i] = max(dp[i - 1], dp[i - 2] + num[i - 1])

其中，dp[i]表示打劫到第i间房屋时累计取得的金钱最大值。

时间复杂度O(n)，空间复杂度O(n)
'''
class Solution:
    # @l, dictionary where lists all house and their money
    # @return integer
    def robber(self, l):
        s = 0
        for i in range(len(l)):
            if i==0:
                s = l[1]
            elif i+1<len(l):
                for j in (i+2, len(l)+1):
                    s += self.robber(l[j:])
        
        
        return s
        
    # @param num, a list of integer
    # @return an integer
    def rob(self, num):
        size = len(num)
        dp = [0] * (size + 1)
        if size:
            dp[1] = num[0]
        for i in range(2, size + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + num[i - 1])
        return dp[size]
        
    #观察可知，上述代码的空间复杂度可以进一步化简为O(1)：
    

    # @param num, a list of integer
    # @return an integer
    def rob2(self, num):
        size = len(num)
        odd, even = 0, 0
        for i in range(size):
            if i % 2:
                odd = max(odd + num[i], even)
            else:
                even = max(even + num[i], odd)
        return max(odd, even)

    # @param A: A list of non-negative integers.
    # return: an integer
    def houseRobber(self, A):
        # write your code here
        result = 0
        f, g, f1, g1 = 0, 0, 0, 0
        for x in A:
            f1 = g + x
            g1 = max(f, g)
            g, f = g1, f1
       
        return max(f, g)


    
    
s = Solution()
l = [23,34,56,456,34,444,123,34,3,344]
print (s.rob2(l))

