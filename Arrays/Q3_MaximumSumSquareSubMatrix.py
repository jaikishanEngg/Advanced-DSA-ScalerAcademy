#
# Created on Fri May 13 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
Given a 2D integer matrix A of size N x N, find a B x B submatrix where B<= N and B>= 1, such that the sum of all the elements in the submatrix is maximum.

Problem Constraints
1 <= N <= 103.
1 <= B <= N
-102 <= A[i][j] <= 102.

Input Format
First arguement is an 2D integer matrix A.
Second argument is an integer B.

Output Format
Return a single integer denoting the maximum sum of submatrix of size B x B.

Example Input
Input 1:
 A = [
        [1, 1, 1, 1, 1]
        [2, 2, 2, 2, 2]
        [3, 8, 6, 7, 3]
        [4, 4, 4, 4, 4]
        [5, 5, 5, 5, 5]
     ]
    B = 3

Input 2:
 A = [
        [2, 2]
        [2, 2]
    ]
    B = 2

Example Output
Output 1:
    48
Output 2:
    8

Example Explanation
Explanation 1:
    Maximum sum 3 x 3 matrix is
    8 6 7
    4 4 4
    5 5 5
    Sum = 48

Explanation 2:
 Maximum sum 2 x 2 matrix is
  2 2
  2 2
  Sum = 8
'''
class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        rows = len(A)
        cols = len(A[0])

        #we've to check the maximum sum generated in each sub-matrix of size B*B
        l = 0
        #cols-B = 2; 0,1,2
        while l <= cols-B:
            colPrefixSum = [0]*cols
            for c in range(cols - B + 1):
                endcol = c + B - 1
                for r in range(rows - B + 1):
                    endrow = r + B - 1
                    #calculate prefixsum for the current sub-matrix of sixe B*B
                    colPrefixSum[r][c] += A[r][c]

            
            l += 1

                

s = Solution()
A = [
    [1, 1, 1, 1, 1],
    [2, 2, 2, 2, 2],
    [3, 8, 6, 7, 3],
    [4, 4, 4, 4, 4],
    [5, 5, 5, 5, 5]
    ]
B = 3
s.solve(A,B)








