#
# Created on Mon May 09 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
Given a 2D Matrix A of dimensions N*N, we need to return the sum of all possible submatrices.

Problem Constraints
1 <= N <=30
0 <= A[i][j] <= 10

Input Format
Single argument representing a 2-D array A of size N x N.

Output Format
Return an integer denoting the sum of all possible submatrices in the given matrix.

Example Input
A = [ [1, 1]
      [1, 1] ]

Example Output
16

Example Explanation
Number of submatrices with 1 elements = 4, so sum of all such submatrices = 4 * 1 = 4
Number of submatrices with 2 elements = 4, so sum of all such submatrices = 4 * 2 = 8
Number of submatrices with 3 elements = 0
Number of submatrices with 4 elements = 1, so sum of such submatrix = 4
Total Sum = 4+8+4 = 16
'''
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        #Approach: we will solve this problem using contribution technique.
        #Given a 2-D matrix, A.  we will figure out how many times does the element A[i][j] contributes in all the sub arrays possible. 
        #As we're computing the sum of all sub arrays, n*A[i][j] where n is no.of times contributed.

        #So, we will find out the contribution count by computing using TopLeft and BottomRight cells
        #Lets say if we have 5 rows (0,1,2,3,4) and 6 columns(0,1,2,3,4,5) and we have to find the no.of times A(2,3) has contributed
            #If I start the subarray from A(0,0) then I can end at A(2,3), A(2,4), A(2,5), A(3,3),A(3,4),A(3,5), A(4,3), A(4,4), A(4,5).
            #similarly, if I start the subarray from A(0,1) then again 9 times A(2,3) will be contributed
            #so, from top left 12 times and from bottom right 9 times.  Total 12 * 9 times the element A(2,3) can be contributed.

        #Compute topLeft and bottomRight
        rows = len(A)
        cols = len(A[0])

        ans = 0

        for i in range(rows):
            for j in range(cols):
                topLeft = (i + 1) * (j + 1)
                bottomRight = (rows - i) * (cols - j)
                ans += ((topLeft * bottomRight) * A[i][j])
        
        return ans

s = Solution()
A = [ [1, 1],
      [1, 1] ]
ans = s.solve(A)
assert ans == 16

A = [ [4, 9, 6],
      [5, -1, 2] ]
ans = s.solve(A)
assert ans == 166
