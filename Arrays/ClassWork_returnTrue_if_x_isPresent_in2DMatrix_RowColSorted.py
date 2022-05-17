#
# Created on Tue May 10 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Given N*N Matrix, Row and Columns are sorted. Given a number x, return True if its present in the matrix.
Eg:
10 20 30 40
15 25 35 45
27 29 37 48
32 33 39 50
The elements of the matrix are sorted row wise and column wise also.  x = 35
'''
class Solution:
    def solve(self, matrix, x):
        #We will start from top right corner, and start comparing with it
        n = len(matrix) #no.of rows/cols as its a square matrix
        i = 0
        j = n-1
        while(i < n and j >= 0):
            if x == matrix[i][j]:
                return True
            elif x < matrix[i][j]:
                j -= 1
            elif x > matrix[i][j]:
                i += 1
        return False

s = Solution()
A = [[10, 20, 30, 40],
     [15, 25, 35, 45],
     [27, 29, 37, 48],
     [32, 33, 39, 50]]
x = 35
ans = s.solve(A, x)
assert ans == True #True
x = 19
ans = s.solve(A, x)
assert ans == False #False
