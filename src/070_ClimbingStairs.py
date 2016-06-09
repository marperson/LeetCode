#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on Jun 9, 2016
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. 
In how many distinct ways can you climb to the top? 
解题思路：
比如说，如果是3层，可以有[[1,1,1],[1,2],[2,1]]共3种方法
n层的方法数 = n - 1层的方法数 + n - 2层的方法数。
爬楼梯问题。经典的动态规划问题。每次上一个台阶或者两个台阶，问一共有多少种方法到楼顶。
这个实际上就是斐波那契数列的求解。可以逆向来分析问题，
如果有n个台阶，那么走完n个台阶的方式有f(n)种。而走完n个台阶有两种方法，先走完n-2个台阶，
然后跨2个台阶；先走完n-1个台阶，然后跨1个台阶。所以f(n) = f(n-1) + f(n-2)。
@author: frank.he
'''

class Solution:
    def climbingStairs(self, n):
        num = 0
        for i in range(1, n + 1):
            if i == 1:
                num = 1
            elif i == 2:
                num = 2
            else:
                num = self.climbingStairs(i - 1) + self.climbingStairs(i - 2)
                
        return num
    
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        dp = [1 for i in range(n+1)]
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

print (Solution().climbStairs(10))
