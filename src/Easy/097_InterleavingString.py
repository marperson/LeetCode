#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on Apr 20, 2016
判断C串是否有A串和B串组成（就是说C中提取出A之后剩下B）
简单DP，dp[i][j]表示A[1..i]和B[1..j]是否可以组成C[1..i+j]
@author: frank.he
'''
class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        if len(s3) != len(s1) + len(s2):
            return False
        dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i > 0 and dp[i-1][j] and s3[i+j-1] == s1[i-1]:
                    dp[i][j] = True
                elif j > 0 and dp[i][j-1] and s3[i+j-1] == s2[j-1]:
                    dp[i][j] = True
                else:
                    dp[i][j] = False
        return dp[len(s1)][len(s2)]
    

solution = Solution()

print (solution.isInterleave('abc','def','abdcef'))