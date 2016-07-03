#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on Jun 7, 2016
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated. 

注意点：

    该模型不需要填完整，没有填写的用"."表示
    不用关心该模型是否有解，只需要判断现有情况

例子：

输入: board=["..4...63.",".........","5......9.","...56....","4.3.....1","...7.....","...5.....",".........","........."] 输出: false
解题思路

用三个列表表示横向、纵向和小正方形的情况。特别需要注意的是小正方形内的元素的表示方法：board[i/3*3+j/3][i%3*3+j%3]。

Rule:
1. Current row has not same value
2. Current column has not same value
3. Current cube has not same value

@author: frank.he
'''

class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        row = [set([]) for i in range(9)]
        col = [set([]) for i in range(9)]
        grid = [set([]) for i in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if board[r][c] in row[r]:
                    return False
                if board[r][c] in col[c]:
                    return False

                g = r / 3 * 3 + c / 3
                if board[r][c] in grid[g]:
                    return False
                grid[g].add(board[r][c])
                row[r].add(board[r][c])
                col[c].add(board[r][c])

        return True
    
    def isValidSudoku2(self, board):
        # Verify if current value already exists in row or column
        def isValid(x, y, tmp):
            # Current row has not same value
            for i in range(9):
                if board[i][y]==tmp:return False
            # Current column has not same value
            for i in range(9):
                if board[x][i]==tmp:return False
            # Current cube has not same value
            for i in range(3):
                for j in range(3):
                    if board[(x/3)*3+i][(y/3)*3+j]==tmp: return False
            return True
        for i in range(9):
            for j in range(9):
                # check current value, if it's '.' jump current iteration and continue, otherwise continue below lines
                if board[i][j]=='.':
                    # jump current iteration, ignore following lines
                    continue    
                # Set current value to variable tmp
                tmp=board[i][j]
                # Set current value to 'D'
                board[i][j]='D'
                # Validate Sudoku, if true then set current value back.
                if isValid(i,j,tmp)==False: 
                    return False
                else:
                    board[i][j]=tmp
        return True
    
    
    def isValidSudoku3(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        point = "."
        for i in range(9):
            row = []
            column = []
            square = []
            for j in range(9):
                element = board[i][j]
                if element != point:
                    if element in row:
                        return False
                    else:
                        row.append(element)

                element = board[j][i]
                if element != point:
                    if element in column:
                        return False
                    else:
                        column.append(element)

                element = board[i // 3 * 3 + j // 3][i % 3 * 3 + j % 3]
                if element != point:
                    if element in square:
                        return False
                    else:
                        square.append(element)
        return True


board = ["..4...63.",".........","5......9.","...56....","4.3.....1","...7.....","...5.....",".........","........."]
print (Solution().isValidSudoku3(board))
